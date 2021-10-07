import click

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

if __name__=="__main__":
    main()
     