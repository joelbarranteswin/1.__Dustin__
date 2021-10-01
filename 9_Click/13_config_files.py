import click
import click_config_file

@click.command()
@click.option('--name','-n',help="especifica el nombre")
@click.option('--location', '-l',help="especifica la localizacion")
@click_config_file.configuration_option()
def main(name, location):
    """un simple CLI"""
    click.echo("Hello {}".format(name))
    click.echo("your location is {}".format(location))
    

if __name__ == '__main__':
    main()

