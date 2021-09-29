# arguments is essential and necesary
import click

@click.command()
@click.argument('number1', type=int)
@click.argument('number2', type=int)
@click.argument('operador')
# ,default='suma',type=click.Choice(['suma','resta','division','multiplicacion']))

def main(number1, number2, operador):
    """A simple CLI with pos ARG"""
    click.echo("a calculator")
    if operador=='suma':
        resultado = number1 + number2
    elif operador=='resta':
        resultado = number1 - number2
    elif operador=='division':
        resultado = number1 / number2
    elif operador=='multiplicacion':
        resultado = number1 * number2    
    click.echo("el resultado es ", resultado)

if __name__ == "__main__":
    main()


