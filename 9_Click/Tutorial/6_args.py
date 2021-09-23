import click
from pyfiglet import Figlet


#Enter
@click.group()
def main():
    pass


@main.command(name='1')
@click.option('--name','-n', type=int, prompt='introduce un numero')
def names(name):
    print('el numero es {}'.format(sum(name)))




@main.command(name='2')
@click.option('--about')
def info(about):
	""" About NLPiffy """
# STYLED NAME with Figlet
	f = Figlet(font="slant")
	print(f.renderText("Silocy Data"))


if __name__ == '__main__':
    main()