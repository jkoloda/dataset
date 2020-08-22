import os


def is_leaf(folder):
    """Determine whether folder does not contain any subfolders.

    Parameters
    ----------
    folder : str
        Folder to be checked for being a leaf.

    Returns
    -------
    bool
        True if folder is leaf (does not contain any subfolders),
        False otherwise.

    """
    content = [os.path.join(folder, f) for f in os.listdir(folder)]
    content = [c for c in content if os.path.isdir(c)]
    if len(content) == 0:
        return True
    else:
        return False


def check_filename_by_extension(filename, include=None, exclude=None):
    """Check whether file extension is in include/exclude list.

    Parameters
    ----------
    filename : str
        Filename to be checked.

    include : list
        List of allowed extensions (without colon), case insensitive.

    exclude : list
        List of not allowed extensions (without colon), case insensitive.

    Returns
    -------
    bool
        True if filename extension is in include list, False if filename
        extension is in exclude list.

    """
    assert not (include is not None and exclude is not None)
    if include is not None:
        include = ['.' + i.lower() for i in include]
        if os.path.splitext(filename)[-1].lower() not in include:
            return False

    if exclude is not None:
        exclude = ['.' + e.lower() for e in exclude]
        if os.path.splitext(filename)[-1].lower() in exclude:
            return False

    return True


def check_filename_by_pattern(filename, include=None, exclude=None):
    """Check whether filename contain specific pattern.

    Parameters
    ----------
    filename : str
        Filename to be checked.

    include : list
        List of allowed patterns.

    exclude : list
        List of not allowed patterns.

    Returns
    -------
    bool
        True if filename contains any pattern from include list, False if
        filename contains any pattern from exclude list.

    """
    assert not (include is not None and exclude is not None)
    if include is not None:
        if any([i.lower() in filename.lower() for i in include]) is False:
            return False

    if exclude is not None:
        if any([e.lower() in filename.lower() for e in exclude]) is False:
            return False

    return True
