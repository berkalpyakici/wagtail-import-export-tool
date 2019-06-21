import tempfile

def null_pks():
    """
    Nullifies primary keys within all supplied fields.

    Arguments:
    fields -- Dictionary of all fields.

    Returns:
    N/A. Overwrites the argument.
    """
    pass

def null_fks():
    """
    Nullifies foreign keys within all supplied fields.

    Arguments
    fields -- Dictionary of all fields.

    Returns:
    N/A. Overwrites the argument.
    """
    pass

def zip_contents():
    """
    Creates and returns a zip archive of all supplied items.
    """
    pass

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