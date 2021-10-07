import click

@click.command()
@click.option('--name','-n')
def main(name):
    """un simple CLI"""
    click.echo(click.style("Hello {}".format(name), 
                fg='blue',bg='white', bold=True))
    # click.secho==click.echo + click.style
    click.secho("your name is {}".format(name),
                fg='yellow')
    click.echo("your name is: " + click.style(name, fg='red'))

if __name__ == '__main__':
    main()