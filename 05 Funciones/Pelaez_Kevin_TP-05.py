#Ejercicios Funciones

# 1)
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2)
def saludar_usuario(nombre):
    print(f"Hola, {nombre}!")

# 3)
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4)
def calcular_area_circulo(radio):
    area = 3.1416 * float(radio) * float(radio)
    print("El area del circlo es: ", area)

def calcular_perimetro_circulo(radio):
    perimetro = 3.1416 * float(radio) * 2
    print("El perimetro del ciruclo es: ",perimetro)

# 5)
def segundos_a_horas(segundos):
    return float(segundos) / 3600

# 6)
def tabla_multiplicar(numero):

    for i in range(1,11):
        print(f"{i} x {numero} = {i * numero}")

# 7)
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    if b != 0:
        division = a / b
    else:
        division = 0

    return (suma, resta, multiplicacion, division)

# 8)
def calcular_imc(peso, altura):
    return (peso/(altura * altura))

# 9)
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# 10)
def calcular_promedio(a,b,c):
    suma = float(a + b + c)
    promedio = suma / 3
    return promedio



if __name__ == "__main__":
    # Ejercicio 1
    imprimir_hola_mundo()

    # Ejercicio 2
    nombre = input("Introducir tu nombre de usuario: ")
    saludar_usuario(nombre)

    # Ejercicio 3
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su residencia: ")

    informacion_personal(nombre, apellido, edad, residencia)

    # Ejercicio 4
    radio = input("Ingrese la medida del radio del circulo: ")
    calcular_area_circulo(radio)
    calcular_perimetro_circulo(radio)

    # Ejercicio 5

    segs = int(input("Ingrese la cantidad de segundos a convertir: "))
    print(f"{segs} equivalen a {segundos_a_horas(segs)} horas")

    # Ejercicio 6
    numero_tabla = int(input("Ingrese un numero para la tabla de multiplicar: "))
    tabla_multiplicar(numero_tabla)

    # Ejercicio 7

    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese otro numero: "))
    resultados = operaciones_basicas(a, b)
    
    suma, resta, mult, div = resultados
    
    print(f"Valores desglozados:")
    print(f"  Suma: {suma}")
    print(f"  Resta: {resta}")
    print(f"  Multiplicación: {mult}")
    print(f"  División: {div}")


    # Ejercicio 8
    peso = float(input("Ingrese su peso: "))
    altura = float(input("Ingrese su altura: "))

    print(f"Tu indice IMC es: {calcular_imc(peso, altura)}")

    # Ejercicio 9
    celsius = float(input("Ingrese una temperatura en Celcius: "))
    print(f"La temperatura convertida a Fahrenheit es: {celsius_a_fahrenheit(celsius)}")

    # Ejercicio 10
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))
    num3 = int(input("Ingrese un numero: "))
    
    print(f"El promedio de esos numeros es: {calcular_promedio(num1,num2,num3)}")


