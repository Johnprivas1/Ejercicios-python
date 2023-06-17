""""
Problema 1:
Implemente un programa que solicite al usuario una fracción, con formato X/Y, donde cada uno de X e Y es un número entero, y luego
muestra, como un porcentaje redondeado al número entero más cercano, donde se indicará la cantidad de combustible en el
tanque. Se debe tener en cuenta los siguientes casos:
- Colocar E en caso X/Y sea menor a 1% del total
- Colocar F en caso X/Y sea mayor a 99%.
- En otro caso, devolver el valor en porcentaje %
También debe tomar en cuenta los siguientes casos:
- X y Y deben ser números enteros
- X debe ser mayor o igual a Y, y Y != 0
De no cumplirse estos casos, se debe volver a preguntar al usuario. Asegúrese de detectar cualquier excepción como ValueError o ZeroDivisionError.
Ejemplos:
- Input: 4/0 Acción: Volver a preguntar al usuario dada la excepción ZeroDivisionError
- Input 1.5/3 Acción: Error dado que solo se permiten números enteros ValueError
- Input 5/4 Acción: Volver a preguntar al usuario
- Input 3/4 Output: 75%
- Input 4/4: Output F
Nota: Le será de utilidad aplicar
try:
except ValueError:
except ZeroDivisionError:
"""

def calcular_porcentaje_fraccion(fraccion):
    numerador, denominador = fraccion
    porcentaje = (numerador / denominador) * 100

    if porcentaje < 1:
        return 'E'
    elif porcentaje > 99:
        return 'F'
    else:
        return f'{round(porcentaje)}%'


def ingresar_fraccion():
    while True:
        fraccion = input("Ingresa una fracción en formato X/Y: ")
        partes = fraccion.split("/")
        if len(partes) == 2:
            try:
                numerador = int(partes[0])
                denominador = int(partes[1])
                if numerador >= denominador and denominador != 0:
                    return numerador, denominador
                else:
                    print("Error: X debe ser mayor o igual a Y, y Y no puede ser cero.")
            except ValueError:
                print("Error: Los valores ingresados no son números enteros.")
        else:
            print("Error: Formato de fracción inválido.")

# Programa principal
while True:
    try:
        fraccion = ingresar_fraccion()
        resultado = calcular_porcentaje_fraccion(fraccion)
        print("La cantidad de combustible en el tanque es:", resultado)
        break
    except ValueError as e:
        print(f"Error: {str(e)}")
    except ZeroDivisionError as e:
        print("Error: El denominador no puede ser cero.")

"""
Problema 2:
Cree un programa que solicite al usuario una lista de calificaciones separadas por comas. Divida
la cadena en calificaciones individuales y almacénelas en una lista para luego convertir cada
calificación en un entero. Deberá utilizar una sentencia try/except para informar al usuario
cuando los valores introducidos no puedan ser convertidos debido a un error de tipeo o
formato. (Los métodos de cadena le serán de utilidad
"""
calificaciones = input("Ingrese una lista de calificaciones separadas por comas: ")
lista_calificaciones = calificaciones.split(',')
calificaciones_enteros = []
for calificacion in lista_calificaciones:
    try:
        calificacion_entero = int(calificacion)
        calificaciones_enteros.append(calificacion_entero)
    except ValueError:
        print(f"Error: La calificación '{calificacion}' no es un número válido.")

print("Calificaciones en enteros:", calificaciones_enteros)

"""
Problema 3:
Escribe una función de Python que imprima las primeras n filas del triángulo de Pascal.
Nota: El triángulo de Pascal es una figura aritmética y geométrica imaginada por primera vez
por Blaise Pascal.
"""
def triangulo_de_pascal(n):
    if n <= 0:
        print("El número de filas debe ser mayor que cero.")
        return

    triángulo = []
    for i in range(n):
        fila = [1] * (i + 1)
        for j in range(1, i):
            fila[j] = triángulo[i - 1][j - 1] + triángulo[i - 1][j]
        triángulo.append(fila)

    for fila in triángulo:
        print(' '.join(map(str, fila)))
n_filas=int(input("Ingrese filas "))
triangulo_de_pascal(n_filas)

"""
Problema 4:
Escriba una función que, dado un string, retorne la longitud de la última palabra. Se considera
que las palabras están separadas por uno o más espacios. También podría haber espacios al
principio o al final del string pasado por parámetro.
"""
def longitud_ultima_palabra(string):
    
    string = string.strip()        
    palabras = string.split()        
    if len(palabras) > 0:       
        ultima_palabra = palabras[-1]
        return len(ultima_palabra)
    else:     
        return 0
palabra=input("Ingrese un texto: ")
longitud = longitud_ultima_palabra(palabra)
print("Longitud de la última palabra:", longitud)



