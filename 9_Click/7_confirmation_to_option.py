import click

# @click.command()
# @click.argument('file_name',required=True)
# def download(file_name):
#     """download File"""
#     click.confirm("Do yo want to continue donwloading", 
#                     abort=True, default=True)
#     click.echo("downloading {}".format(file_name))
    

# method 2
@click.command()
@click.argument('file_name',required=True)
@click.confirmation_option(prompt="Do yo want to continue donwloading")
def download(file_name):
    """download File"""
    click.echo("downloading {}".format(file_name))


if __name__=='__main__':
    download()