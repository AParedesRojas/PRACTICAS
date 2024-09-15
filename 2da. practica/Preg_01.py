# Crear una clase llamada Persona donde sus atributos deben ser nombre, edad,
# saldo y de nacionalidad peruana y un metodo para solicitar su nombre y edad.

class Persona:
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.nacionalidad = "Peruana"

    def solicitar_datos():
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        sueldo = float(input("Ingrese su sueldo: "))
        return Persona(nombre, edad, sueldo)

    # Metodo para solicitar nombre y edad
    def mostrar_nombre_edad(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Tendrá un metodo cumpleaños donde cada vez que invoque aumentará en un año
# la edad de la persona.

    def cumpleaños(self):
        self.edad += 1
        print(f"¡Hola  {self.nombre}! Ahora tienes {self.edad} años.")

#Crear la instancia de la clase Persona y usar su metodo aumentoSueldo para incrementar
#su sueldo en un 30% (mínimo instanciar la clase 2 veces, mostrar por pantalla dicho
#sueldo ya incrementado).

    def aumentoSueldo(self):
        print(f"Sueldo antes del incremento: {self.sueldo}")
        self.sueldo += self.sueldo * 0.30
        print(f"Sueldo después del incremento: {self.sueldo}")


#Crear un metodo que retorne un mensaje donde indique que:
# “En el año 2025 tendrá XX años”, el año se ingresará por parámetro y la edad es la edad
# que ya se ingresó (Mostrar por pantalla este valor)

    def edad_en_anio(self, anio):
        edad_futura = self.edad + (anio - 2024)
        print(f"En el año {anio}, {self.nombre} tendrá {edad_futura} años.")

print("Datos de la primera persona:")
persona1 = Persona.solicitar_datos()

print("\nMostrando nombre y edad:")
persona1.mostrar_nombre_edad()

print("\nIncrementando sueldos:\n")
persona1.aumentoSueldo()

print("\nEdad en el año 2025:\n")

persona1.edad_en_anio(2025)




