# Eric Thortsen, https://github.com/sonofthort/multi_unzip_py, MIT License

import sys
import os
import shutil

directory = sys.argv[1]

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    if os.path.isfile(file):
        name = os.path.splitext(filename)[0]
        newDir = os.path.join(directory, name)
        try:
            shutil.unpack_archive(file, newDir)
            os.remove(file)
        except:
            # fail silently; assume this is not an archive or is not meant to be unpacked by this script
            pass
