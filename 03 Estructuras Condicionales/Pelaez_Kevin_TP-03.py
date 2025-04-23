#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.*/

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")


# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

nota = int(input("Ingrese su nota:"))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.


numero = int(input("Ingrese un numero:"))

if numero % 2 == 0:
    print("Ha ingreso un numero par")
else: 
    print("Por favor, ingrese un numero par")


# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece: niño menor 12, adolescentes entre 1 y 18, adulto joven entre 18 y 30, adulto mayor a 30



edad = int(input("Ingrese su edad: "))

if edad >= 30:
    print("Categoria Adulto/a")
elif edad >= 18:
    print("Categoria Adulto/a joven")
elif edad >= 12:
    print("Categoria Adolescente")
else:
    print("Categoria Niño/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

contraseña = str(input("Ingrese una contraseña entre 8 y 14 caracteres: "))

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor ingrese una contraseña de entre 8 y 14 caracteres")


# 6) Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.


from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1,100) for i in range(50)]

moda = mode(numeros_aleatorios)
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)

print("Considerando los siguientes valores: ")
print(numeros_aleatorios)
print("La media: ", media)
print("La moda: ", moda)
print("La mediana: ", mediana)

if media > mediana and mediana > moda:
    print("La distribucion normal es de SESGO POSITIVO")
elif media < mediana and mediana <moda:
    print("La distribucion normal es de SESGO NEGATIVO")
elif media == mediana and moda == mediana:
    print("La distribucion normal no tiene sesgo")
else:
    print("Los resultados no tienen categoria")


# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

frase = str(input("Ingrese una frase o palabra: "))

if frase[len(frase)-1] == 'a' or frase[len(frase)-1] == 'e' or frase[len(frase)-1] == 'i' or frase[len(frase)-1] == 'o' or frase[len(frase)-1] == 'u':
    print(frase + "!")
else:
    print(frase)


# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee


nombre = str(input("Ingrese su nombre: "))

print("\nIngrese una eleccion del siguiente Menu:")
print("1.Quiere su nombre en mayúsculas")
print("2.Quiere su nombre en minúsculas")
print("3.Quiere su nombre con la primera letra mayúscula")

eleccion = int(input("\nElige Opcion: "))

if eleccion == 1:
    print(nombre.upper())
elif eleccion == 2:
    print(nombre.lower())
elif eleccion == 3:
    print(nombre.title())
else:
    print("Ha ingresado una opcion incorrecta")


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud >= 7:
    print("Terremoto Extremo (puede causar graves daños a gran escala)")
elif magnitud >= 6:
    print("Terremoto Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 5:
    print("Terremoto Fuerte (puede causar daños en estructuras debiles)")
elif magnitud >= 4:
    print("Terremoto Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 3:
    print("Terremoto Leve (ligeramente perceptible)")
elif magnitud > 0:
    print("Terremoto Muy Leve (imperceptible)")
else: 
    print("Valor ingresado incorrecto")


# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = str(input("Ingrese en que hemisferio se encuentra N/S: "))

mes = int(input("Ingrese el mes del año (1-12): "))
dia = int(input("Ingrese que dia es (1-31): "))

if (dia >= 21 and mes == 12) or (dia < 20 and mes == 3) or mes == 1 or mes == 2:
    if hemisferio == 'N':
        print("Esta en Invierno")
    else: 
        print("Esta en Verano")
elif (dia >= 21 and mes == 3) or (dia < 20 and mes == 6) or mes == 4 or mes == 5:
    if hemisferio == 'N':
        print("Esta en Primavera")
    else: 
        print("Esta en Otoño")
elif (dia >= 21 and mes == 6) or (dia < 20 and mes == 9) or mes == 7 or mes == 8:
    if hemisferio == 'N':
        print("Esta en Verano")
    else: 
        print("Esta en Invierno")
elif (dia >= 21 and mes == 9) or (dia < 20 and mes == 12) or mes == 10 or mes == 11:
    if hemisferio == 'N':
        print("Esta en Otoño")
    else: 
        print("Esta en Primavera")

