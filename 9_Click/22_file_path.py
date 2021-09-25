import click
from pathlib import Path




@click.command()
@click.option('--filename', type=click.Path(exists=True))
def touch(filename):
    """Print FILENAME if the file exists."""
    print(Path(filename).parent.resolve())
    # click.echo(click.format_filename(filename))

if __name__ == '__main__':
    touch()