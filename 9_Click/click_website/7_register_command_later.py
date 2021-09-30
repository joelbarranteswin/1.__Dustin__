import click

@click.command()
def greet():
    click.echo("Hello, World!")

@click.group()
def group():
    pass

group.add_command(greet)

if __name__ == '__main__':
    group()
