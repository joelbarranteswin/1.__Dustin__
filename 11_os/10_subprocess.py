import os
import subprocess
import sys

#py_filepath = 'C:/Users/benb/Desktop/flaskEconServer/plots.py'
py_filepath = 'joel.py'

args = '"%s" "%s" "%s"' % (sys.executable,                  # command
                           py_filepath,                     # argv[0]
                           os.path.basename(py_filepath))   # argv[1]

proc = subprocess.run(args)
print('returncode:', proc.returncode)