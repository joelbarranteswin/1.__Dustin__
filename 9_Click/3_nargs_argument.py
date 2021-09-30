import click


# Variadic Argument /Multiple Argument
@click.command()
@click.argument('source',nargs=-1) #accept infinite number of values
# @click.argument('source',nargs=2)# accept unlimited number of values
@click.argument('destination')
def main(source,destination):
	"""A Simple CLI with Variadic Argument"""
	for f in source:
		click.echo("Moving {} to folder {}".format(source,destination))

if __name__ == '__main__':
	main()