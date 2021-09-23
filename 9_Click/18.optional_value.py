import click

# @click.command()
# @click.option("--name", is_flag=False, flag_value="Flag", default="Default")
# def hello(name):
#     click.echo(f"Hello, {name}!")

@click.command()
@click.option('--name', prompt=True, prompt_required=False, default="Default")
def hello(name):
    click.echo(f"Hello {name}!")



if __name__ == "__main__":
    hello()