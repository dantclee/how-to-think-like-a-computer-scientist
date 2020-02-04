import os

def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def print_path(path, prefix = ""):
    """ Print recursive listing of path """
    if prefix == "":  # Detect outermost call, print a heading
        print("Path listing for", path)

    dirlist = get_dirlist(path)
    for file in dirlist:
        fullname = os.path.join(path, file)   # Turn name into full pathname
        if os.path.isdir(fullname):        # If a directory, recurse.
            print_path(fullname, prefix + "| ")
        else:
            print(fullname)  # Print the path

path = input('Enter path: ')
print(print_path(path))
