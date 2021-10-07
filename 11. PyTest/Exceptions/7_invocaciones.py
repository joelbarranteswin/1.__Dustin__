
def mi_funcion(algo=None):
    try:
        if algo is None: #es true
            raise ValueError("Error! No se permite un valor nulo") ##llama al error
    except ValueError:
        print("Error! No se permite un valor nulo (desde la excepción)")

mi_funcion()
