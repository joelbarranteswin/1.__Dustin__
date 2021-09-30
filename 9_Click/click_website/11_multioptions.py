import click

# @click.command()
# @click.option('--pos', nargs=2, type=float)
# def findme(pos):
#     a, b = pos
#     click.echo(f"{a} / {b}")



# @click.command()
# @click.option('--item', type=(str, int))
# def putitem(item):
#     name, id = item
#     click.echo(f"name={name} id={id}")



# @click.command()
# @click.option('--item', nargs=2, type=click.Tuple([str, int]))
# def putitem(item):
#     name, id = item
#     click.echo(f"name={name} id={id}")


# @click.command()
# @click.option('--message', '-m', multiple=True)
# def commit(message):
#     click.echo('\n'.join(message))


# @click.command()
# @click.option('-v', '--verbose', count=True)
# def log(verbose):
#     click.echo(f"Verbosity: {verbose}")

# @click.command()
# @click.option('/debug;/no-debug')
# def log(debug):
#     click.echo(f"debug={debug}")


#Command prompt

@click.command()
@click.option('--name', prompt='name please')
def hello(name):
    click.echo(f"Hello {name}!")



# @click.command()
# @click.option('--name', prompt='your name please')
# def hello(name):
#     click.echo(f"Hello {name}!")



if __name__ == '__main__':
    hello()

#python .\11_multioptions.py