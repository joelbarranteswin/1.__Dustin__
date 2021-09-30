import click

@click.command()
@click.argument('name')
@click.option('--number', type=int, help= 'help message here')

def main(name, number):
    '''
    help message
    '''
    for i in range(number):
        print(f'hello {name}')

if __name__=='__main__':
    main()