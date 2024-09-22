from datetime import datetime

def conteo(func):
    def wrapper(*args, **kwargs):
        cantidad_parametros = len(args) + len(kwargs)

        # evaluar que deba ser mayor que 1
        if cantidad_parametros > 1:
            print(f"Se han usado {cantidad_parametros} parámetros en la función.")
        else:
            print("Debe haber más de 1 parámetro para procesar la función.")
            return

        # Al final de la función decorada indicar mediante un mensaje
        # que función fue ejecutada:

        resultado = func(*args, **kwargs)
        print(f"La función '{func.__name__}' ha sido ejecutada.")

        return resultado

    return wrapper


# Función decorada para registrar una persona
@conteo
def registrar_persona(edad, nombre):
    hora_actual = datetime.now().hour
    minuto_actual = datetime.now().minute
    print(f"Registrando a {nombre}, de {edad} años. Hora: {hora_actual}:{minuto_actual}")


# Crear otra función que será decorada y que calculará la media de 4 notas:

@conteo
def calcular_media(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"La media de las 4 notas es: {media}")
    return media

registrar_persona(25, "Antonela")
calcular_media(15, 18, 16, 17)