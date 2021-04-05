#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

#Metodo math
import math

# Variable global utilizada para el ejercicio de nota
notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

# Variable global utilizada para el ejercicio de temperaturas
temp_dataloger = [12.8, 18.6, 14.5, 20.8, 12.1, 21.2, 13.5, 18.6,
                  14.7, 19.6, 11.2, 18.4]


def ej1():
    print('Comenzamos a ponernos serios!')

    '''
    Realice un programa que pida por consola dos números que representen
    el principio y fin de una secuencia numérica.
    Realizar un bucle "for" que recorra esa secuencia armada con "range"
    y cuente cuantos números ingresados hay, y la sumatoria de todos los números
    Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    sino que va hasta el anterior
    '''

    # inicio = ....
    # fin = ....
    inicio = int(input("Ingrese el primer número: "))
    fin = int(input("Ingrese el segundo número: "))

    # cantidad_numeros ....
    cantidad_numeros = 0
    # sumatoria ....
    sumatoria = 0
    # bucle.....

    for i in range(inicio,fin):

        sumatoria += i
 
    cantidad_numeros += len(range(inicio,fin))

    print(sumatoria)
    print(cantidad_numeros)
    print("")
    promedio = sumatoria/cantidad_numeros
    print("El promedio es:",promedio)
    
    # Al terminar el bucle calcular el promedio como:
    # promedio = sumatoria / cantidad_numeros

    # Imprimir resultado en pantalla
    #realizado



def ej2():
    print("Mi Calculadora (^_^)")

    '''
    Tome el ejercicio de clase:
    <condicionales_python /  ejercicios_profundizacion / ej3>,
    copielo a este ejercicio y modifíquelo, ahora se deberá ejecutar
    indefinidamente hasta que como operador se ingrese la palabra "FIN",
    en ese momento debe terminar el programa

    Se debe debe imprimir un cartel de error si el operador ingresado no es
    alguno de lo soportados o no es la palabra "FIN"
    '''
 
    print("Ingrese un número")
    num1 = float(input(": "))
    print("")
    print("Ingrese otro número")
    num2 = float(input(": "))
    #operations

    print("Qué operación deseas realizar?")
    print("Ingresa '+' para suma")
    print("Ingresa '-' para resta")
    print("Ingresa '*' para multiplicación")
    print("Ingresa '/' para división")
    print("Ingresa '**' para potencia")

    operator = str(input(": "))
    
    if operator == "+":
        suma = num1 + num2
        print("El resultado de su suma es:",suma)
    elif operator == "-":
        resta = num1 - num2
        print("El resultado de su resta es:",resta)
    elif operator == "*":
        multiplicacion = num1 * num2
        print("El resultado de su multiplicación es:",multiplicacion)
    elif operator == "/":
        division = num1 - num2
        print("El resultado de su división es:",division)
    elif operator == "**":
        potencia = num1 ** num2
        print("El resultado de su potencia es:",potencia)
    else:
        print("Ninguna de las opciones es correcta, elige otra operación:")
        print("Ingresa '+' para suma")
        print("Ingresa '-' para resta")
        print("Ingresa '*' para multiplicación")
        print("Ingresa '/' para división")
        print("Ingresa '**' para potencia")
    
    print("Quiéres salir de la calculadora? ingrese la palabra FIN:")
    print("Sino presiona enter para seguir en la caluladora")

    break_point = str(input()).capitalize()

    if break_point == "Fin":
        pass
    else:
        ej2()
    #realizado



def ej3():
    print("Mi organizador académico (#_#)")

    '''
    Tome el ejercicio de "calificaciones":
    <condicionales_python / ejercicios_practica / ej3>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Las notas del estudinte se encuentran almacenadas en una
    lista llamada "notas" que ya hemos definido al comienzo del archivo

    Debe calcular el promedio de todas las notas y luego transformar
    la califiación en una letra según la escala establecida en el ejercicio
    "calificaciones" <condicionales_python / ejercicios_practica / ej3>

    A medida que recorre las notas, no debe considerar como válidas aquellas
    que son negativas, en ese caso el alumno estuvo ausente

    Debe contar la cantidad de notas válidas y la cantidad de ausentes
    '''

    # Para calcular el promedio primero debe obtener la suma
    # de todas las notas, que irá almacenando en esta variable
    sumatoria = 0           # Ya le hemos inicializado en 0
    cantidad_notas = 0      # Aquí debe contar cuantas notas válidas encontró
    cantidad_ausentes = 0   # Aquí debe contar cuantos ausentes hubo

    # Realice aquí el bucle para recorrer todas las notas
    # y calcular la sumatoria

    # Terminado el bucle calcule el promedio como
    # promedio = sumatoria / cantidad_notas

    # Utilice la nota promedio calculada y transformela
    # a calificación con letras, imprima en pantalla el resultado

    # Imprima en pantalla al cantidad de ausentes

    #comienzo de ejercicio

    for i in range(len(notas)):
        sumatoria += notas[i]

        if notas[i] < 0:
            print("El alúmno número",i,"estuvo ausente en el examen:","Nota",notas[i])
            cantidad_ausentes +=1

    cantidad_notas = len(notas) - cantidad_ausentes
    puntaje = sumatoria / cantidad_notas
    print("")
    print("La cantidad de notas válidas en el examen fueron:",cantidad_notas)
    print("")
    print("La cantidad de ausentes en el examen fueron:",cantidad_ausentes)
    print("")
    print("El promedio de aprobados fue de:",puntaje)

    # Verifique la calificación de un estudiante según su
    # puntaje en un examen

    # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es mayor a 60       --> imprimir F

    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados

    if puntaje >= 90:
        print("Felicidades! su nota es: A")
    elif puntaje >= 80:
        print("Felicidades! su nota es: B")
    elif puntaje >= 70:
        print("Felicidades! su nota es: C")
    elif puntaje >= 60:
        print("Felicidades! su nota es: D")
    elif puntaje > 60:
        print("Felicidades! su nota es: F")
    else:
        print("Lo siento, no has aprobado :(",puntaje)
    #realizado



def ej4():
    print("Mi primer pasito en data analytics")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_profundizacion /ej5>,
    copielo a este ejercicio y modifíquelo para cumplir el
    siguiente requerimiento

    En este ejercicio se lo provee de una lista de temperatuas,
    esa lista de temperatuas corresponde a los valores de temperaturas
    tomados durante una temperorada del año en Buenos Aires.
    Usted deberá analizar dicha lista para deducir
    en que temporada del año se realizó el muestreo de temperatura.
    La variable con la lista de temperaturas se llama "temp_dataloger"
    definida al comienzo del archivo

    Debe recorrer la lista "temp_dataloger" y obtener los siguientes
    resultados

    1 - Obtener la máxima temperatura
    2 - Obtener la mínima temperatura
    3 - Obtener el promedio de las temperatuas

    Los resultados se deberán almacenar en las siguientes variables
    que ya hemos preparado para usted.
    
    NOTA: No se debe ordenar la lista de temperaturas, se debe obtener
    el máximo y el mínimo utilizando los mismos métodos vistos
    durante la clase (ejemplos_clase)
    '''

    temperatura_max = None      # Aquí debe ir almacenando la temp máxima
    temperatura_min = None      # Aquí debe ir almacenando la temp mínima
    temperatura_sumatoria = 0   # Aquí debe ir almacenando la suma de todas las temp
    temperatura_promedio = 0    # Al finalizar el loop deberá aquí alamcenar el promedio
    temperatura_len = 0         # Aquí debe almacenar cuantas temperatuas hay en la lista

    # Colocar el bucle aqui......

    for i in temp_dataloger:
        temperatura_sumatoria += i
        
        if temperatura_max == None or i > temperatura_max:
            temperatura_max = i

        if temperatura_min == None or i < temperatura_min:
            temperatura_min = i

    temperatura_len = len(temp_dataloger)

    # Al finalizar el bucle compare si el valor que usted calculó para
    # temperatura_max y temperatura_min coincide con el que podría calcular
    # usando la función "max" y la función "min" de python
    # función "max" --> https://www.w3schools.com/python/ref_func_max.asp
    # función "min" --> https://www.w3schools.com/python/ref_func_min.asp
    
    max_1 = max(temp_dataloger)
    min_2 = min(temp_dataloger)

    #print(max_1,min_2)

    # Al finalizar el bucle debe calcular el promedio como:
    # temperatura_promedio = temperatura_sumatoria / cantidad_temperatuas
    
    temperatura_promedio = temperatura_sumatoria / temperatura_len

    print("La temperatura máxima es:",temperatura_max)
    print("La temperatura mínima es:",temperatura_min)
    print("El promedio de temperaturas es:",temperatura_promedio)
    # Corroboren los resultados de temperatura_sumatoria
    # usando la función "sum"
    # función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp
    suma = sum(temp_dataloger)
    #print(suma)
    #print(temperatura_sumatoria)
    '''
    Una vez que tengamos nuestros valores correctamente calculados debemos
    determinar en que epoca del año nos encontramos en Buenos Aires utilizando
    la estadística de años anteriores. Basados en el siguiente link realizamos
    las siguientes aproximaciones:

    verano -->      min = 19, max = 28
    otoño -->       min = 11, max = 20
    invierno -->    min = 8, max = 14
    primavera -->   min = 10, max = 24

    Referencia:
    https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o
    '''
    max_floor = math.floor(temperatura_max)
    min_floor = math.floor(temperatura_min)

    if (min_floor < 21 and min_floor > 17) and (max_floor < 30 and max_floor > 26):
        print("Estamos en verano!")
    elif (min_floor < 13 and min_floor > 9) and (max_floor < 22 and max_floor > 18):
        print("Estamos en otoño!")
    elif (min_floor < 10 and min_floor > 6) and (max_floor < 16 and max_floor > 12):
        print("Estamos en invierno!")
    elif (min_floor < 12 and min_floor > 8) and (max_floor < 26 and max_floor > 22):
        print("Estamos en primavera!")
    
    # En base a los rangos de temperatura de cada estación,
    # ¿En qué época del año nos encontramos?
    # Imprima el resultado en pantalla
    # Debe utilizar temperatura_max y temperatura_min para definirlo
    #realizado



def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_profundizacion / ej4>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Realize un programa que corra indefinidamente en un bucle, al comienzo de la
    iteración del bucle el programa consultará al usuario con el siguiente menú:
    1 - Obtener la palabra más grande por orden alfabético (usando el operador ">")
    2 - Obtener la palabra más grande por cantidad de letras (longitud de la palabra)
    3 - Salir del programa

    En caso de presionar "3" el programa debe terminar e informar por
    pantalla de que ha acabado,
    en caso contrario si se presionar "1" o "2" debe continuar con la siguiente tarea

    NOTA: Si se ingresa otro valor que no sea 1, 2 o 3 se debe enviar
    un mensaje de error y volver a comenzar el bucle
    (vea en el apunte "Bucles - Sentencias" para encontrar
    la sentencia que lo ayude a cumplir esa tarea)

    Si el bucle continua (se presionó "1" o "2") se debe ingresar a otro bucle
    en donde en cada iteración se pedirá una palabra. La cantidad de iteración
    (cantidad de palabras a solicitar) lo dejamos a gusto del alumno, intente que esa
    condición esté dada por una variable (ej: palabras_deseadas = 4)
    Cada palabra ingresada se debe ir almacenando en una lista de palabras, dicha lista la debe inicializar vacia y agregar cada nuevo valor con el método "append".
    Luego de tener las palabras deseadas almacenadas en una lista de palabras
    se debe proceder a realizar las siguientes tareas:

    Si se ingresa "1" por consola se debe obtener la palabra
    más grande por orden alfabético
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra
    más grande alfabeticamente.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?

    Si se ingresa "2" por consola se debe obtener la palabra
    con mayor cantidad de letras
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra con
    mayor cantidad de letras.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?
    
    NOTA: No se debe ordenar la lista de palabras, se debe obtener
    el máximo utilizando los mismos métodos vistos durante la clase
    (ejemplos_clase), tal como el ejercicio anterior. Ordenar una
    lista representa un problema mucho más complejo que solo
    buscar el máximo.

    NOTA: Es recomendable que se organice con lápiz y papel para
    hacer un bosquejo del sistema ya que deberá utilizar 3 bucles en total,
    1 - El bucle principal que hace que el programa corra hasta ingresar un "3"
    2 - Un bucle interno que corre hasta socilitar todas las palabras deseadas
        que se deben ir guardando en una lista
    3- Otro bucle interno que corre luego de que termine el bucle "2" que
       recorre la lista de palabras y busca la mayor según el motivo ingresado ("1" o "2")
  '''
    arr = []
    a = [1,2,3]

    for i in a:
        word = str(input
        ("Ingrese una palabra: "))
        
        arr.append(word)
    
    print("Presiona '1' para ordenar alfabéticamente las palabras")
    print("Presiona '2' para ordenar de mayor a menor cantidad de letras")
    print("Presiona '3' para salir del programa")
    operator = int(input(": "))
    
    
    while False:
        if operator == 1:
            if (arr[0] >= arr[1]) and (arr[0] >= arr[2]):
                print("1:",arr[0])
                if (arr[1] >= arr[2]):
                    print("2:",arr[1])
                    print("3:",arr[2])
                else:
                    print("2:",arr[2])
                    print("3:",arr[1])
            elif (arr[1] >= arr[0]) and (arr[1] >= arr[2]): 
                print("1:",arr[1])
                if (arr[0] >= arr[2]):
                    print("2:",arr[0])
                    print("3:",arr[2])
                else:
                    print("2:",arr[2])
                    print("3:",arr[0])
            elif (arr[2] >= arr[0]) and (arr[2] >= arr[1]):
                print("1:",arr[2])
                if (arr[0] >= arr[1]):
                    print("2:",arr[0])
                    print("3:",arr[1])
                else:
                    print("2:",arr[1])
                    print("3:",arr[0])

        elif operator == 2:
            if len(arr[0]) > len(arr[1]) and len(arr[0]) > len(arr[2]):
                print("1:",arr[0])
                if len(arr[1]) > len(arr[2]):
                    print("2:",arr[1])
                    print("3:",arr[2])
                else:
                    print("2:",arr[2])
                    print("3:",arr[1])
            elif len(arr[1]) > len(arr[0]) and len(arr[1]) > len(arr[2]):
                print("1:",arr[1])
                if len(arr[0]) > len(arr[2]):
                    print("2:",arr[0])
                    print("3:",arr[2])
                else:
                    print("2:",arr[2])
                    print("3:",arr[0])
            elif len(arr[2]) > len(arr[0]) and len(arr[2]) > len(arr[1]):
                print("1:",arr[2])
                if len(arr[0]) > len(arr[1]):
                    print("2:",arr[0])
                    print("3:",arr[1])
                else:
                    print("2:",arr[1])
                    print("3:",arr[0])
        elif operator == 3:
            print("Hasta luego!")
            break
        else:
            print("Ingresa una opción válida")
            operator = int(input(": "))
    #realizado
    print(arr)


if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
