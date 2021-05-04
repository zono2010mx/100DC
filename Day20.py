precio = input("Introduce el precio del producto con dos decimales:  ")
print(precio[:precio.find('.')], "Euros y", precio[precio.find('.')+1:], "Centavos")