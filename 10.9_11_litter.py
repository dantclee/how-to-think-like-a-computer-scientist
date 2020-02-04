import os

def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.

      IMPORTANT: This exercise is not finished. 
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def create_files(path):
    """ create files in all directories of path """
    #if prefix == "":  # Detect outermost call, print a heading
    #    print("Folder listing for", path)
    #    prefix = "| "

    dirlist = get_dirlist(path)
    print(dirlist)
    for file in dirlist:
        #print(prefix+file)                    # Print the line
        fullname = os.path.join(path, file)   # Turn name into full pathname
        if os.path.isdir(fullname):        # If a directory, recurse.
            create_files(fullname)
        else:
            print('reach else clause')
            fullname += 'trash.txt'
            os.open(fullname, mode ='w')

path = input('Enter path: ')
create_files(path)
