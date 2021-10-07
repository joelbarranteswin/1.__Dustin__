import click

@click.command()
@click.option('--weather', type=click.Choice(['sunny', 'rainy', 'snowy']), prompt='introduce una eleccion ')
@click.option('--valor', type=click.Choice(['e', 'w', 'r']), prompt='introduce una eleccion ')
def main(weather, valor):
    print(f'I love it when the weather is {weather}')

if __name__ == '__main__':
    main()
