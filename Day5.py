#Programa Dia 5

Peso=int(input("Introduce tu peso: "))
Altura=float(input("Introduce tu altura: "))

IMC=Peso/(Altura * Altura)

print("Tu indice de masa corporal es: {0:.2f}".format(IMC))