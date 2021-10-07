import click

#metodo 1
@click.command()
@click.option('--firstname','-f', prompt=True)
@click.option('--password','-p',prompt=True,
            hide_input=True,confirmation_prompt=True)
def main(firstname,password):
    """un simple CLI"""
    click.echo("your firstname is {}".format(firstname))
    click.echo("your pasword is {}".format(password))

# #Metodo 2
# @click.command()
# @click.option('--firstname','-f', prompt="enter your name")
# def main(firstname):
#     """un simple CLI"""
#     click.echo("your firstname is {}".format(firstname))

# #metodo 3
# @click.command()
# def main():
#     """un simple GUI"""
#     fname = click.prompt("enter your firstname")
#     click.echo("your firstname is {}".format(fname))


if __name__=='__main__':
    main()
