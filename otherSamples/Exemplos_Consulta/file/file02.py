import os
from os import walk
import time
import glob

def is_locked(filepath):
    """Checks if a file is locked by opening it in append mode.
    If no exception thrown, then the file is not locked.
    """
    locked = None
    file_object = None
    if os.path.exists(filepath):
        try:
            print(f"Trying to open {filepath}.")
            buffer_size = 8
            # Opening file in append mode and read the first 8 characters.
            file_object = open(filepath, 'a', buffer_size)
            if file_object:
                print(f"{filepath} is not locked.")
                locked = False
        except IOError in message:
            print(f"File is locked (unable to open in append mode).\n {message}")
            locked = True
        finally:
            if file_object:
                file_object.close()
                print(f"{filepath} closed.")
    else:
        print(f"{filepath} not found.")
    return locked

def wait_for_files(filepaths):
    """Checks if the files are ready.

    For a file to be ready it must exist and can be opened in append
    mode.
    """
    wait_time = 5
    for filepath in filepaths:
        # If the file doesn't exist, wait wait_time seconds and try again
        # until it's found.
        while not os.path.exists(filepath):
            print(f"{filepath} hasn't arrived. Waiting {wait_time} seconds.")
            time.sleep(wait_time)
        # If the file exists but locked, wait wait_time seconds and check
        # again until it's no longer locked by another process.
        while is_locked(filepath):
            print(f"{filepath} is currently in use. Waiting {wait_time} seconds.")
            time.sleep(wait_time)

# Test
if __name__ == '__main__':
    files = [r"testfile1.json",
             r"testfile2.json"]
    #print(wait_for_files(files))
    myPath = '*.json'
    myFile = []
    myCount= 0
    a = glob.glob(myPath)
    for (dirpath, dirname, filenames) in walk(myPath):
        for myFiles in filenames:
            if '.txt' in myFiles:
                myFile.append(myFiles)

    if not a:
        print('vazio')
    else:
        print(f"O valor de a é: {a}")

    print(myFile)
