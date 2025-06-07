# Ejercicios

# 1)
print("================Ejercicio 1================")
def factorial(num):
    if num == 0:
        return 1
    else:
        resultado = num * factorial(num - 1)
    
    return resultado

numero = int(input("Ingrese un numero para calcular el factorial: "))

while numero > 0:
    print("El factorial del numero es: ",factorial(numero))
    numero -=1


# 2)
print("================Ejercicio 2================")

def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion-1) + fibonacci(posicion-2)
    
pos = int(input("Ingrese un numero para calcular Fibonacci: "))

while pos >= 0:
    print(f"La sucesion de Fibonacci de la posicion {pos} es: ",fibonacci(pos))
    pos -=1

# 3)
print("================Ejercicio 3================")

def potenciacion(base, exponente):

    if base==0:
        return 0
    elif exponente == 0:
        return 1
    else:
        resultado = base * potenciacion(base, exponente-1)
        return resultado
    

base = int(input("Ingrese un numero base: "))
exponente = int(input("Ingrese un exponente: "))

print(f"el numero {base} elevado a la {exponente} es: ",potenciacion(base, exponente))

# 4)
print("================Ejercicio 4================")

def numero_a_decimal(decimal):
    binario = ""

    if (decimal == 0):
        return "0"
    elif (decimal == 1):
        return "1"
    else:
        resto = decimal % 2
        cociente = decimal // 2

        binario = numero_a_decimal(cociente) + str(resto)
        return binario

# 5) 
print("================Ejercicio 5================")

def es_palindromo(palabra):
    
    if len(palabra) <= 1:
        return True
    
    if(palabra[0] != palabra[-1]):
        return False
    
    return es_palindromo(palabra[1:-1])

print("Probar funcion: ", es_palindromo("radar"))

# 6)
print("================Ejercicio 6================")
def suma_digitos(numero):
    if (numero < 10):
        return numero
    
    ultimo_digito = numero % 10
    resto = numero // 10

    return ultimo_digito + suma_digitos(resto)
# 7)
print("================Ejercicio 7================")
def contar_bloques(num):
    if num == 1:
        return 1
    
    return num + contar_bloques(num-1)

print("Probar: ", contar_bloques(4))

# 8)
print("================Ejercicio 8================")
def contar_digito(numero, digito):
    if numero < 10:
        if (numero == digito):
            return 1
        else:
            return 0
    
    ultimo_digito = numero % 10
    resto_del_numero = numero // 10
    
    if ultimo_digito == digito:
        coincidencia = 1
    else:
        coincidencia = 0
    
    return coincidencia + contar_digito(resto_del_numero, digito)