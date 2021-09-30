import click
import pandas
from joel import *


@click.version_option(version="0.0.1-silocydata", prog_name="generator catv, smatv and fo reports")
@click.group()
def main():
    """ generator catv, smatv and fo reports: 
        a simple tool to organize and sort files into folders
	"""
    pass


@main.command(name='darit')
@click.option('--numero', '-n', nargs=2)
def sum(numero):
    """Simplemete usa un script y suma dos valores
    """
    print(f'este es el valor{numero}')
    # click.echo(numero, fg='blue')

    

@main.command(name='excel_catv')
def excel_catv():
    pass


if __name__ == "__main__":
    main()




#darit report catv path --format (excel | json) --out outpath
#darit report smatv path --format (excel | json) --out outpath
#darit report fo path --format (excel | json) --out outpath