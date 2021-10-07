import click
from click_plugins import with_plugins
from pkg_resources import iter_entry_points

#parent
@with_plugins(iter_entry_points('click_command_tree'))
@click.group()
def main():
    """"""
    pass



#hijo
@main.group()
def reverse():
    """vuelta del texto"""


#hijo del hijo
@reverse.command('mayuscula')
@click.argument('name')
def reverse_upper(name):
    """vuelta and mayuscula del texto"""
    click.echo(name[::-1].upper())

@reverse.command('minuscula')
@click.argument('name')
def reverse_lower(name):
    """vuelta and mayuscula del texto"""
    click.echo(name[::-1].lower())

#hijo
@main.group()
def capitalize():
    pass

#hijo del hijo
@capitalize.command('mayuscula')
@click.argument('name')
def capitalize_upper(name):
    """mayuscula de texto"""
    click.echo(name.upper())

if __name__=="__main__":
    main()      