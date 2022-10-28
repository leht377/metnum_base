def args_type_checking(fn):
    def wrapper(*args):

        argumentos = {
            "f(x)": args[0],
            "intervaloA": args[1],
            "intervaloB": args[2],
            "tolerancia": args[3],
        }

        if not callable(argumentos["f(x)"]):
            raise TypeError("El objeto no es invocable")

        if not isinstance(argumentos["intervaloA"], (int, float)):
            raise TypeError("El intervaloA deben ser enteros o floats")

        if not isinstance(argumentos["intervaloB"], (int, float)):
            raise TypeError("El intervaloB deben ser enteros o floats")

        if not isinstance(argumentos["tolerancia"], (int, float)):
            raise TypeError("El intervaloC deben ser enteros o floats")

        return fn(*args)

    return wrapper
