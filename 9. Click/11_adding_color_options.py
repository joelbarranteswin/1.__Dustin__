##### 
#pip install click-help-colors

import click
from click_help_colors import HelpColorsGroup, HelpColorsCommand

@click.group(cls=HelpColorsGroup,
            help_headers_color='yellow',
            help_options_color='magenta')
def main():
    "un CLI simple"
    pass

@main.command(cls=HelpColorsGroup,
            help_headers_color='red')
@click.option('--name','-n',help='Specify Name')
def sayhello(name):
    """say hello"""
    click.echo("say hello {}".format(name))

if __name__ == "__main__":
    main()
