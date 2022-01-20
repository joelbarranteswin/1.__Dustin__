import pandas
from pathlib import Path
path = Path(Path.cwd(), 'PROYECTO_fo.xlsx')
print(str(path))
excel = pandas.read_excel(path)
print(excel)
