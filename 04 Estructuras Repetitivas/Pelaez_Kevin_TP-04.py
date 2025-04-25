# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(101):
    print(i)


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero  = int(input("Ingrese un numero: "))
resto = -1
exponente = 0

while resto != numero:
    exponente += 1
    resto = numero % ( 10 ** exponente)

print("La cantidad de digitos es: ", exponente)

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

numero_ingresado_uno = int(input("Ingrese un numero: "))
numero_ingresado_dos = int(input("Ingrese un numero: "))
sumador = 0

if(numero_ingresado_uno > numero_ingresado_dos):
    cota_inferior = numero_ingresado_dos
    cota_superior = numero_ingresado_uno
else:
    cota_inferior = numero_ingresado_uno
    cota_superior = numero_ingresado_dos


for i in range(cota_inferior + 1, cota_superior):
    sumador += i

print("La suma de numeros comprendidos es: ",sumador)

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0

numero = int(input("Ingrese un numero: "))
sumador = 0

while numero != 0:
    sumador += numero

    numero = int(input("Ingrese un numero: "))

print("La suma de toda la secuencia es: ",sumador)


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero_a_adivinar = random.randint(0, 9)
numero = -1
intentos = 0

print("Adivina un número entre 0 y 9.")

while numero != numero_a_adivinar:
    numero = int(input("Introduce tu número: "))
    intentos += 1
    
print("Has acertado el número.")
print(f"Cantidad de intentos: {intentos}")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100,-2,-2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

numero = int(input("Ingrese un numero: "))
sumador = 0

for i in range(numero+1):
    sumador += i

print(f"La suma de los numeros comprendidos entre el 0 y {numero} es: {sumador}")


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio)

contador_pares = 0
contador_impares = 0
contador_negativos = 0
contador_positivos = 0

for i in range(100):
    numero = int(input("Ingrese un numero: "))

    if numero >= 0:
        contador_positivos += 1
        if numero % 2 == 0:
            contador_pares += 1
        else: 
            contador_impares += 1
    else:
        contador_negativos += 1
        if numero % 2 == 0:
            contador_pares += 1
        else: 
            contador_impares += 1


print("La cantindad de numeros pares es: ", contador_pares)
print("La cantindad de numeros impares es: ", contador_impares)
print("La cantindad de numeros positivos es: ", contador_positivos)
print("La cantindad de numeros negativos es: ", contador_negativos)

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

sumador = 0

for i in range(100):
    numero = int(input("Ingrese un numero: "))
    sumador += numero

media = sumador / 100.0

print("La media de los valores ingresados es: ",media)


# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero  = int(input("Ingrese un numero: "))
numero_original = numero
numero_al_reves = 0


while numero != 0:
    digito = numero % 10

    numero_al_reves = numero_al_reves * 10 + digito

    numero = numero // 10

print(f"El numero ingresado es: {numero_original}")
print(f"El numero al reves es: {numero_al_reves}")