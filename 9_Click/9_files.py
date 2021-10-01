import click

@click.group()
def main():
    """un cimple CLI"""
    pass

@main.command()
@click.argument('url')
def open_url(url):
    """Open Url"""
    click.echo("Opening URL")
    click.launch(url)

@main.command()
@click.argument('file')
@click.option('--locate','-l',default=False)
def open_file(file,locate):
    """Open File """
    click.echo("Opening File")
    click.launch(file, locate=locate)

if __name__ == "__main__":
    main()