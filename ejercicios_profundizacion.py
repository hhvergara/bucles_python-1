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
    inicio = int(input("Ingrese el primer número de la secuencia\n"))
    # fin = ....
    fin = int(input("Ingrese el último número de la secuencia\n"))
    
    # cantidad_numeros ....
    cantidad_numeros = 0

    # sumatoria ....
    suma = 0

    # bucle.....
    for i in range(inicio,fin + 1):
        cantidad_numeros +=1
        suma += i


    # Al terminar el bucle calcular el promedio como:
    # promedio = sumatoria / cantidad_numeros
    prom = suma / cantidad_numeros

    # Imprimir resultado en pantalla
    print("La sumatoria de la secuencia es:", suma, "\n"
          "El promedio de la secuencia es:", prom, "\n")

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
    operator = True
    operator_list = ["+", "-", "*", "/", "**"]

    while operator != "FIN":

        numero_1 = float(input("Ingrese el primer número\n"))
        numero_2 = float(input("Ingrese el segundo número\n"))
        operator = str(input("Ingrese el símbolo del operador matemático\n"
                             "- Para Suma (+)\n"
                             "- Para Resta (-)\n"
                             "- Para Multiplicación (*)\n"
                             "- Para División (/)\n"
                             "- Para Exponente/Potencia (**)\n"))
        
        if operator not in operator_list:
            print("\033[93mERROR: ¡Operador matemático equivocado!\n"
                  "Inténtelo nuevamente\033[0m\n")
            continue

        if operator == "+":
            operation = numero_1 + numero_2
            print("El resultado de {} {} {} es: ".format(numero_1, operator, numero_2),"\n"
                  "{}\n".format(operation))


        elif operator == "-":
            operation = numero_1 - numero_2
            print("El resultado de {} {} {} es: ".format(numero_1, operator, numero_2),"\n"
                  "{}\n".format(operation))


        elif operator == "*":
            operation = numero_1 * numero_2
            print("El resultado de {} {} {} es: ".format(numero_1, operator, numero_2),"\n"
                  "{0:.2f}\n".format(operation))


        elif operator == "/":
            operation = numero_1 / numero_2
            print("El resultado de {} {} {} es: ".format(numero_1, operator, numero_2),"\n"
                  "{0:.2f}\n".format(operation))

        elif operator == "**":
            operation = numero_1 ** numero_2
            print("El resultado de {} {} {} es: ".format(numero_1, operator, numero_2),"\n"
                  "{0:.2f}\n".format(operation))


        operator = str(input("- Presione cualquier tecla para realizar un nuevo cálculo:\n"
                             "- Para finalizar el programa escriba la palabra: (FIN)\n").upper())    

    print("Hasta la Próximaaa (°v°)\n")

def ej3():
    print("Mi organizador académico (#_#)")

    '''
    Tome el ejercicio de "calificaciones":
    <condicionales_python / ejercicios_practica / ej3>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento

    Las notas del estudiante se encuentran almacenadas en una
    lista llamada "notas" que ya hemos definido al comienzo del archivo

    Debe caluclar el promedio de todas las notas y luego transformar
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
    # y cacular la sumatoria

    for i in notas:
        sumatoria += i # --> En la sumatoria no tienen que estar considerados los negativos.
        if i >= 0:
            cantidad_notas += 1
        elif i < 0:
            cantidad_ausentes += 1

    # Terminado el bucle calcule el promedio como
    # promedio = sumatoria / cantidad_notas

    prom = sumatoria / cantidad_notas # aquí estas tomando la sumatoria considerando los negativos sobre la cantidad
    # de notas que NO considera los negativos!

    # Utilice la nota promedio calculada y transformela
    # a calificación con letras, imprima en pantalla el resultado

    if prom >= 90:
        nota = "A"
    
    elif prom >= 80:
        nota = "B"
   
    elif prom >=70:
        nota = "C"
    
    elif prom >=60:
        nota = "D"

    else:
        nota = "F"

    # Imprima en pantalla la cantidad de ausentes
    
    print("Calificación Final:", nota, "\n"
          "Su nota promedio es: {0:.2f}".format(prom), "\n" 
          "Y la cantidad de ausentes es de:", cantidad_ausentes, "\n")

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
    Ustede deberá analizar dicha lista para deducir
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
    
    temperatura_max = temp_dataloger[0]
    temperatura_min = temp_dataloger[0]

    for i in temp_dataloger:

        temperatura_len += 1
        temperatura_sumatoria += i

        if i > temperatura_max:
            temperatura_max = i
        elif i < temperatura_min:
            temperatura_min = i

    # Al finalizar el bucle compare si el valor que usted calculó para
    # temperatura_max y temperatura_min coincide con el que podría calcular
    # usando la función "max" y la función "min" de python
    # función "max" --> https://www.w3schools.com/python/ref_func_max.asp
    # función "min" --> https://www.w3schools.com/python/ref_func_min.asp

    if temperatura_max == max(temp_dataloger) and temperatura_min == min(temp_dataloger):
        print("Coindide ambos valores")

    # Al finalizar el bucle debe calcular el promedio como:
    # temperatura_promedio = temperatura_sumatoria / cantidad_temperatuas

    temperatura_promedio = temperatura_sumatoria / temperatura_len
    print("La temperatura promedio es: {0:.2f}".format(temperatura_promedio))

    # Corroboren los resultados de temperatura_sumatoria
    # usando la función "sum"
    # función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp

    if temperatura_sumatoria == sum(temp_dataloger):
        print("Coincide ambos valores")
        
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

    # En base a los rangos de temperatura de cada estación,
    # ¿En qué época del año nos encontramos?
    # Imprima el resultado en pantalla
    # Debe utilizar temperatura_max y temperatura_min para definirlo

    verano_min = 19
    verano_max = 28
    otoño_min = 11
    otoño_max = 20
    invierno_min = 8
    invierno_max = 14
    primavera_min = 10
    primavera_max = 24

    if temperatura_min >= verano_min and temperatura_max <= verano_max:
        print("Nos encontramos en Verano\n")
    elif temperatura_min >= otoño_min and temperatura_max <= otoño_max:
        print("Nos encontramos en Otoño\n")
    elif temperatura_min >= invierno_min and temperatura_max <= invierno_max:
        print("Nos encontramos en Invierno\n")
    else:
        print("Nos encontramos en Primavera\n")

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
    Cada palabra ingresada se debe ir almacenando en una lista de palabras, dicha
    lista la debe inicializar vacia y agregar cada nuevo valor con el método "append".
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
    el máximo utilizando el mismos métodos vistos durante la clase
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
    operation = True
    operation_list = ["1", "2", "3"]

    while operation != "3":
        words_list = []
        operation = str(input("Ingrese el número de la acción que desea realizar:\n"
                             "1 - Obtener la palabra más grande por orden alfabético\n"
                             "2 - Obtener la palabra más grande por cantidad de letras\n"
                             "3 - Salir del programa\n"))
        
        if operation not in operation_list:
            print("\033[93mERROR: ¡Número de operación incorrecto!\n"
                  "Inténtelo nuevamente\033[0m\n")
            continue

        elif operation == "1" or operation == "2":
            for i in range(4):
                num_word = 1 + i
                word = str(input("Ingrese la palabra {}:".format(num_word)))
                words_list.append(word)
            
            if operation == "1":
                biggest_word = max(words_list)
                print("La palabra más grande por orden alfabético es:", biggest_word.upper(), "\n")

            elif operation == "2":
                longest_word = max(words_list, key = len)
                print("La palabra mayor por cantidad de letras es:", longest_word.upper(), "\n")

    print("Hasta la Próximaaa: Programa Finalizado! (°v°)")

if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
