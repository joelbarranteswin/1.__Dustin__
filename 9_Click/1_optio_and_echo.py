import click

@click.command()
@click.option("--valor")
def main(valor):
    click.echo(valor)

if __name__=="__main__":
    main()