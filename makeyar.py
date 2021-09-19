import os
import glob

read_files = glob.glob("*.yar")

with open("result1.yar", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

root_dir = ""  # path to the root directory to search
for root, dirs, files in os.walk(root_dir, onerror=None):  # walk the root dir
    for filename in files:  # iterate over the files in the current dir
        file_path = os.path.join(root, filename)  # build the file path
        try:
            read_files = glob.glob(file_path)
            for f in read_files:

                print(read_files)
                with open("result.yar", "wb") as outfile:
                    with open(f, "rb") as infile:
                        outfile.write(infile.read())

        except (IOError, OSError):  # ignore read and permission errors
            pass
        # open the file for reading

import shutil

with open("result1.yar", 'wb') as outfile:
    for filename in glob.glob('*.yar'):
        if filename == "result1.yar":
            # don't want to copy the output into the output
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)