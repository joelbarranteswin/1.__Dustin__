import click

@click.command()
@click.option('--from', '-f', 'from_',)
@click.option('--to', '-t')
def reserved_param_name(from_, to):
    click.echo(f"from {from_} to {to}")

if __name__ == '__main__':
    reserved_param_name()