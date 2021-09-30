import click

@click.command()
@click.option('--n', type=int, show_default=True, help='escribe cualqui numero')
def dots(n):
    click.echo('.' * n)

if __name__ == '__main__':
    dots()