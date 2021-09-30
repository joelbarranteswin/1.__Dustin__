import click

@click.group()
def cli():
    pass

@cli.group()
def lunch():
    pass

@cli.group()
def dinner():
    pass

@lunch.command()
def burger():
    print(f'enjoy your burger')

@dinner.command()
def burger():
    print(f'enjoy your burger')



# @click.command()
# def burger():
#     print(f'enjoy your burger')

# lunch.add_command(burger)
# dinner.add_command(burger)


if __name__=='__main__':
    cli()