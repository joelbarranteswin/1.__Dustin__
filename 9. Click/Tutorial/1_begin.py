import click

@click.group()
@click.version_option(version='0.01',prog_name='file_organizer')
def main():
	""" File Organizer: a simple tool to organize and sort files into folders
	"""
	pass


if __name__ == "__main__":
    main()