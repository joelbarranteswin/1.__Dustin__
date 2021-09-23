import click

# @click.command()
# @click.argument('src', envvar='SRC', type=click.File('r'))
# def echo(src):
#     """Print value of SRC environment variable."""
#     click.echo(src.read())


@click.command(context_settings={"ignore_unknown_options": True})
@click.argument('files', nargs=-1, type=click.Path())
def touch(files):
    """Print all FILES file names."""
    for filename in files:
        click.echo(filename)


if __name__ == '__main__':
    touch()