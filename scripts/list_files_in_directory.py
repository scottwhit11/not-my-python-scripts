# list_files_in_directory.py

# to read directory, the Import os module
import os

# directory path 
_path = '/home/tuts/Documents'

# Reading file content's
_files = os.listdir(_path)

# Print directory's content

for _file in _files:
  print(_file)