import click
import codecs

# @click.command()
# @click.option(
#     "--password", prompt=True, hide_input=True,
#     confirmation_prompt=True
# )
# def encode(password):
#     click.echo(f"encoded: {codecs.encode(password, 'rot13')}")



# @click.command()
# @click.password_option()
# def encrypt(password):
#     click.echo(f"encoded: to {codecs.encode(password, 'rot13')}")



import os

@click.command()
@click.option(
    "--username", prompt=True,
    default=lambda: os.environ.get("USER", ""),
    show_default="current user"
)
def hello(username):
    click.echo(f"Hello, {username}!")



if __name__ == '__main__':
    # encode()
    # encrypt()
    hello()