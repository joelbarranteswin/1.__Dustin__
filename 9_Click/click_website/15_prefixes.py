import click

# @click.command()
# @click.option('+w/-w')
# def chmod(w):
#     click.echo(f"writable={w}")

# if __name__ == '__main__':
#     chmod()


@click.command()
@click.option('/debug;/no-debug')
def log(debug):
    click.echo(f"debug={debug}")

if __name__ == '__main__':
    log()
