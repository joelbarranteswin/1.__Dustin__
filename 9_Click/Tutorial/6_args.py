import click
from pyfiglet import Figlet


#Enter
@click.group()
@click.version_option(version="0.0.1-silocydata", prog_name="generator catv, smatv and fo reports")
def main():
    """
    Silocy Data Present:

            Command Line-Interface reports catv, smatv and fo
    
    """
    pass


@main.command(name='1')
@click.option('--name','-n', type=int, prompt='introduce un numero')
def names(name):
    print('el numero es {}'.format(sum(name)))






@main.command()
@click.option('--about')
def info(about):
	f = Figlet(font="slant")
	print(f.renderText("Silocy Data"))


if __name__ == '__main__':
    main()

