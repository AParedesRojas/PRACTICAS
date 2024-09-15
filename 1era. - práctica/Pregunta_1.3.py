nombre= "Margarita"
salario= 3450.50
edad= 25
compania= "MI NEGOCIO SAC"

#BONOS
bono_1=0.10
bono_2=0.05

#potencia de salario:
potencia_salario= salario**2

#bonos finales

bono_final1= potencia_salario + (salario*bono_1)
bono_final2= potencia_salario + (salario*bono_2)

if edad > 30:
    print("Usted tiene un bono de 10% en el mes de diciembre")
    print("El bono final es: {} ".format(bono_final1))

else:
    print("Usted tiene un bono de 5% en el mes de diciembre")
    print("El bono final es: {} ".format(bono_final2))
