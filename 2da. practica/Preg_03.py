class BilleteraElectronica:
    def __init__(self, nombre, apellido, saldo_soles, saldo_dolares):
        self.nombre = nombre
        self.apellido = apellido
        self.saldo_soles = saldo_soles
        self.saldo_dolares = saldo_dolares
        self.tipo_cambio = 3.8

# Mostrar los saldos actuales:

    def mostrar_saldos(self):
        print(f"{self.nombre} {self.apellido}:")
        print(f"Saldo en soles: S/ {self.saldo_soles}")
        print(f"Saldo en dólares: $ {self.saldo_dolares}\n")

# Transferir entre cuentas (de soles a dólares o viceversa):

    def transferir(self, monto, de_soles_a_dolares=True):
        if de_soles_a_dolares:
            if self.saldo_soles >= monto:
                self.saldo_soles -= monto
                self.saldo_dolares += monto / self.tipo_cambio
                print(f"Se transfirió S/ {monto} a $ {monto / self.tipo_cambio:.2f}")
            else:
                print(f"No hay suficiente saldo en soles para transferir S/ {monto}")
        else:
            if self.saldo_dolares >= monto:
                self.saldo_dolares -= monto
                self.saldo_soles += monto * self.tipo_cambio
                print(f"se transfirio $ {monto} a S/ {monto * self.tipo_cambio:.2f}")
            else:
                print(f"No hay suficiente saldo en dólares para transferir $ {monto}")
        self.mostrar_saldos()

# Retirar dinero:

    def retirar(self, monto, en_soles=True):
        if en_soles:
            if self.saldo_soles >= monto:
                self.saldo_soles -= monto
                print(f"Se retiró S/ {monto}. Saldo actualizado:")
            else:
                print("Fondos insuficientes para retirar en soles.")
        else:
            if self.saldo_dolares >= monto:
                self.saldo_dolares -= monto
                print(f"Se retiro $ {monto}. Saldo actualizado:")
            else:
                print("Fondos insuficientes para retirar en dólares.")
        self.mostrar_saldos()

# Instanciamos la billetera para un usuario:

billetera1 = BilleteraElectronica("Carlos", "Pérez", 1000, 500)
billetera2 = BilleteraElectronica("Lucía", "Gómez", 2000, 300)

# Mostramos los saldos iniciales
billetera1.mostrar_saldos()
billetera2.mostrar_saldos()

# Realizamos transferencias entre cuentas
print("Transferencias:\n")
billetera1.transferir(500, de_soles_a_dolares=True)
billetera2.transferir(100, de_soles_a_dolares=False)

# Realizamos retiros de dinero

print("\nRetiros:\n")
billetera1.retirar(300, en_soles=True)
billetera2.retirar(50, en_soles=False)