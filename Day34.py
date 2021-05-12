edad= int(input("Ingrese la edad:"))
if edad < 4:
    precion=0
elif edad <= 18:
    precio=4
else:
    precio=10

if edad < 4:
    print("El cliente entra gratis")
else:
    print("El precio de la entrada es", precio, "€.")
