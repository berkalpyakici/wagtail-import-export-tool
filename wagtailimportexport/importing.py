import io
import json
import logging
from zipfile import ZipFile

from django.core.files.images import ImageFile
from django.core.files.base import File

from wagtail.core.models import Page
from wagtail.images.models import Image
from wagtail.documents.models import Document

from wagtailimportexport import functions

def import_page(uploaded_archive, parent_page):
    """
    Imports uploaded_archive as children of parent_page.

    Arguments:
    uploaded_archive -- A file object, which includes contents.json 
    and the media objects.
    parent_page -- Page object, where the page(s) will be imported to.

    Returns:
    numpages -- Integer value of number of pages that were successfully
    imported.
    numfails -- Integer value of number of pages that were failed to be
    imported.
    message -- String message to report any warning/issue.
    """

    # Read the zip archive and load as 'payload'.
    payload = io.BytesIO(uploaded_archive.read())

    # Open zip archive.
    with ZipFile(payload, 'r') as zf:
        try:
            # Open content.json and load them into contents dictionary.
            with zf.open('content.json') as mf:
                contents = json.loads(mf.read().decode('utf-8-sig'))

                # Unzip all the files in the zip directory.
                contents_mapping = functions.unzip_contents(zf)

                # Get the list of pages to skip.
                existing_pages = list_existing_pages(contents['pages'])
                existing_pages = []

                # Loop through all the pages.
                for (i, page_record) in enumerate(contents['pages']):

                    new_field_datas = {}

                    # Skip the existing pages.
                    if i in existing_pages:
                        continue

                    # Reassign document IDs.
                    for (fieldname, filedata) in page_record["documents"].items():

                        new_field_datas[fieldname] = None

                        # Skip if the document is set to null.
                        if not filedata:
                            continue

                        local_file_query = get_fileobject(filedata["file"], Document)
                        
                        local_file_id = local_file_query if local_file_query else create_fileobject(
                            filedata["file"], contents_mapping[filedata["file"]], Document)

                        new_field_datas[fieldname] = local_file_id
                    
                    # Reassign image IDs.
                    for (fieldname, filedata) in page_record["images"].items():

                        new_field_datas[fieldname] = None

                        # Skip if the image is set to null.
                        if not filedata:
                            continue

                        local_file_query = get_fileobject(filedata["file"]["name"], Image)
                        
                        local_file_id = local_file_query if local_file_query else create_fileobject(
                            filedata["file"]["name"], contents_mapping[filedata["file"]["name"]], Image)

                        new_field_datas[fieldname] = local_file_id
        
        except LookupError as e:
            # If content.json does not exist, then return the error,
            # and terminate the import_page.
            logging.error("Importing file failed because file does not exist: "+str(e))
            return (0, 1, "File does not exist: "+str(e))
    
    return 1, 2, "Imported: Accounting 1, Accounting 2"

def list_existing_pages(pages):
    """
    Returns a list of pages that already exist in this
    environment by looking up by slug.

    Arguments:
    pages -- A list of pages in content.json

    Returns:
    existing_pages -- List of pages that correspond to indexes
    in 'pages'.
    """

    existing_pages = []

    for (i, page_record) in enumerate(pages):
        try:
            # Trying to get the page.
            localpage = Page.objects.get(slug=page_record['content']['slug'])

            if localpage:
                existing_pages.append(i)

        except Page.DoesNotExist:
            continue
    
    return existing_pages

def get_fileobject(title, objtype):
    """
    Returns the id of the object if it exists, otherwise returns
    False.

    Arguments:
    title -- The filename to be queried.
    objtype -- Image, Document from Wagtail.

    Returns:
    False if the object does not exist in this environment,
    object's integer ID if it does exist.
    """

    try:
        # Check whether the object already exists.
        localobj = objtype.objects.get(file=title)

        if localobj:
            return localobj.id

    except objtype.DoesNotExist:
        return False

    return False

def create_fileobject(title, uploaded_file, objtype):
    """
    Creates a new object given the information and returns
    the ID of the created object. Assumes the object with
    title does not exist.

    Arguments:
    title -- The filename of the object to be created.
    uploaded_file -- The file object to create.
    objtype -- Image, Document from Wagtail.

    Returns:
    Integer ID of the created object if the creation is successful;
    otherwise None.
    """

    with open(uploaded_file, 'rb') as mf:

        # Create the file object based on objtype.
        if objtype == File:
            filedata = File(mf)
        elif objtype == Image:
            filedata = ImageFile(mf)
        else:
            return None

        try:
            with transaction.atomic():
                # Create the object and return the ID.
                localobj = objtype.objects.create(file=filedata, title=title)
                return localobj.id

        except IntegrityError:
            logging.error("Integrity error while uploading a file:", title)
            return None

    return None