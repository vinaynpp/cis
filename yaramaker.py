import shutil
import glob
import os

root_dir = ""  # path to the root directory to search

for root, dirs, files in os.walk(root_dir, onerror=None):  # walk the root dir
    for filename in files:  # iterate over the files in the current dir
        file_path = os.path.join(root, filename)  # build the file path
        try:
      
            with open("result.yar", "a") as outfile:
                with open(file_path, "r") as infile:
                    outfile.write(infile.read())

        except (IOError, OSError):  # ignore read and permission errors
            pass
        # open the file for reading