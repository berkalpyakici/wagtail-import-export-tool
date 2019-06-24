import tempfile
import zipfile
import os
import io
import json

from django.core.files.storage import get_storage_class
from django.core.serializers.json import DjangoJSONEncoder


def null_pks(page, data):
    """
    Nullifies primary keys within all supplied fields.

    Arguments:
    fields -- Dictionary of all fields.

    Returns:
    N/A. Overwrites the argument.
    """
    pass

def null_fks(page, data):
    """
    Nullifies foreign keys within all supplied fields.

    Arguments
    fields -- Dictionary of all fields.

    Returns:
    N/A. Overwrites the argument.
    """
    pass

def zip_contents(page_contents):
    """
    Creates and returns a zip archive of all supplied items.

    Arguments:
    page_contents -- A list of page dictionaries.

    Returns:
    Zip file to be downloaded by the client.
    """

    file_storage = get_storage_class()()

    # Create a temporary directory.
    with tempfile.TemporaryDirectory() as tempdir:

        # Create a temporary zip.
        zfname = os.path.join(tempdir, 'content.zip')

        # Open the zip archive with write mode.
        with zipfile.ZipFile(zfname, 'w') as zf:

            # Write the main content.json file to store all data.
            zf.writestr(
                'content.json',
                json.dumps(page_contents, indent=2, cls=DjangoJSONEncoder)
            )
            
            # Loop through pages to explore all used images and documents.
            for page in page_contents:

                # Export all the images.
                for image_def in page['images'].values():
                    if not image_def:
                        continue
                    
                    filename = image_def['file']['name']
                    with file_storage.open(filename, 'rb') as f:
                        zf.writestr(filename, f.read())
                
                # Export all the documents.
                for doc_def in page['documents'].values():
                    if not doc_def:
                        continue
                    
                    filename = doc_def['file']
                    with file_storage.open(filename, 'rb') as f:
                        zf.writestr(filename, f.read())
        
        with open(zfname, 'rb') as zf:
            fd = zf.read()

    return io.BytesIO(fd)

def unzip_contents(zip_contents):
    """
    Extracts all items in the zip archive and returns a mapping
    of the contents, as well as their location in tempdir.

    Arguments:
    zip_contents -- Zip file that is in memory.

    Returns:
    Map of the extracted files.
    """

    # Create a temporary directory.
    tempdir = tempfile.mkdtemp()

    # Extract all contents.
    zip_contents.extractall(tempdir)

    # Return the mapping of all extracted members.
    return {member: tempdir+'/'+member for member in zip_contents.namelist()}