import os

with os.scandir('11_os/') as entries:
    for entry in entries:
        print(entry.name)