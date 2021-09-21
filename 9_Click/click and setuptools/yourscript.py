import click

@click.command()
@click.option('--pedido', type=click.Choice(['humitas','torta','caramelos','paneton']))
def cli(pedido):
    """Example script."""
    click.echo(f'Hello World! \nhoy comera {pedido}')

if __name__ == '__main__':
    cli()

