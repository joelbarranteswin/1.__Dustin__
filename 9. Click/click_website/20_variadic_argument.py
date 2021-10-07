import click

@click.command()
@click.argument('src', nargs=-1) #unlimited number is accepted
@click.argument('dst', nargs=1)
def copy(src, dst):
    """Move file SRC to DST."""
    for fn in src:
        click.echo(f"move {fn} to folder {dst}")

if __name__ == '__main__':
    copy()