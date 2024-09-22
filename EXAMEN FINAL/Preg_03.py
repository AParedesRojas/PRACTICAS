import time

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        tiempo_ejecucion = fin - inicio
        print(f"Tiempo de ejecución de '{func.__name__}': {tiempo_ejecucion:.4f}"
              f"segundos")
        return resultado

    return wrapper


# Crear una función, por ejemplo: usando 6 números e indicar el mayor
# de todos ellos:

@medir_tiempo
def sumar_y_encontrar_mayor(**numeros):
    suma = sum(numeros.values())
    mayor = max(numeros.values())
    print(f"Suma total: {suma}")
    print(f"El numero mayor es: {mayor}")
    return suma, mayor


# usando el decorador implementado con un mínimo de 03 ejemplos:

def main():
    # Ejemplo 1 - usando 6 números
    print("\nEjemplo 1:")
    sumar_y_encontrar_mayor(a=15, b=24, c=6, d=43, e=33, f=19)

    # Ejemplo 2 - usando 4 números
    print("\nEjemplo 2:")
    sumar_y_encontrar_mayor(x=124, y=57, z=78, w=91)

    # Ejemplo 3 - usando 3 números
    print("\nEjemplo 3:")
    sumar_y_encontrar_mayor(m=1000, n=2000, o=500)


if __name__ == "__main__":
    main()