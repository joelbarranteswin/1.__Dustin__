# remember install pip install alive-progress

from alive_progress import alive_bar
import time

for x in [100]:
   with alive_bar(x) as bar:
       for i in range(100):
           time.sleep(.03)
           bar()

