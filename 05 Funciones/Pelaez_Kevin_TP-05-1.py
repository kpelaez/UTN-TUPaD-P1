#1
lista1_a_100 = list(range(0,104,4))

#2
lista_2 = ['a','b','c','d','e']
print(lista_2[3])

#3
lista_3 = []
lista_3.append('Hola')
lista_3.append('Programacion')
lista_3.append('uno')
print(lista_3)

#4
animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"

print(animales)

#5
#El programa busca el mayor valor de la lista de enteros y lo elimina con el metodo remove
#Luego imprime la lista por pantalla

#6
lista_6 = list(range(10,31,5))
print(lista_6)

#7
autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "moto"
autos[2] = "bici"

#8
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
#a 
compras[2].append("jugo")

#b
compras[1][1] = "tallarines"

#c
compras[0].remove("pan")

#d
print(compras)

#10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)