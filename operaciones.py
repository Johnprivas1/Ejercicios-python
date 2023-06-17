"""
PROBLEMA 6
"""

def suma():
    try:
        print('='*10,"SUMA",'='*10)
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 + num2
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido"

def resta():
    try:
        print('='*10,"RESTA",'='*10)
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 - num2
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido"

def producto():
    try:
        print('='*10,"MULTIPLICACIÓN",'='*10)
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 * num2
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido"

def division():
    try:
        print('='*10,"DIVISION",'='*10)
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if num2 == 0:
            return "Error: No es posible dividir entre cero"
        resultado = num1 / num2
        return resultado
    except ValueError:
        return "Error: Tipo de dato no válido"
