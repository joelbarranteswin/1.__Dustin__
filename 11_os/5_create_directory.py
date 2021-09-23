import os
# os.mkdir('11_os/') #create un file afuera



# from pathlib import Path
# p = Path('11_os/new_dir') #se crea un nuevo directorio
# os.makedirs('2018/10/05') # para crear muchos directorios internos
# p.mkdir()


from pathlib import Path

p = Path('11_os/new')
p.mkdir(exist_ok=True)