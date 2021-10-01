import click

def recursive_help(cmd,parent=None):
    ctx=click.core.Context(cmd,info_name=cmd.name,parent=parent)
    print(cmd.get_help(ctx))
    print()
    commands = getattr(cmd,"commands",{})
    for sub in commands.values():
        recursive_help(sub,ctx)

#el padre
@click.group()
def main(): 
    """un simple CLI with group"""
    pass

@main.command()
@click.argument('text')
def reverse(text):
    """el reverso de un texto"""
    click.echo(text[::-1])

@main.command()
@click.argument('text')
def capitalize(text):
    """mayuscula a un texto"""
    click.echo(text.upper())

@main.command()
def show_help():
    """Muestra todas las ayudas """
    recursive_help(main)

if __name__=="__main__":
    main()