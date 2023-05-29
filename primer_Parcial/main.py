import json
import re

def verificar_miembro_salon_de_la_fama(lista_jugador,indice):
    '''Recibe la lista de jugadores y el indice del jugador
    -Verifica que el jugador tenga un logro "Miembro del salon de la fama"
    -Muestra la informacion del jugador y su logro, en caso que no lo tenga muestra que no tiene dicho logro'''
    for jugador in lista_jugador[indice - 1:indice]:
        print("------------------------------------------------------------------")
        cadena = (jugador['logros'])
        logros = "\n".join(cadena)
        validar_salon_de_la_fama = re.search(r"([Miembro]+) ([del]+) ([Salon]+) ([de]+) ([la]+) ([Fama]+) ([del]+) ([Baloncesto]+)",logros)
        if validar_salon_de_la_fama != None:
            print("Nombre: ",jugador['nombre'])
            print("Miembro del Salon de la Fama de Baloncesto")
        else:
            print("No pertenece al salon de la fama de baloncesto")

        print("------------------------------------------------------------------")

def calcular_mostrar_jugador_mas_logros(lista_jugador:list):
    '''Recibe la lista de jugadores
    -Calcula los logros entre todos los jugadores y lo guarda en una variable
    -Devuelve la cantidad de logros y el nombre del jugador con mas logros'''
    jugador_con_mas_logros = 0
    nombre_jugador_mas_logros = None
    for jugador in lista_jugador:
        if len(jugador['logros']) > jugador_con_mas_logros:
            jugador_con_mas_logros = len(jugador['logros'])
            nombre_jugador_mas_logros = jugador['nombre']
    print("--------------------------")
    print("Nombre: ",nombre_jugador_mas_logros)
    print("Cantidad de Logros: ",jugador_con_mas_logros)

def calcular_mostrar_menor_promedio(lista_jugador:list):
    '''Recibe la lista de jugadores
    -Suma todos lo promedios de puntos totales y le resta el promedio mas bajo
    -Devuelve el promedio de todos los puntos totales y tambien el promedio de todos los puntos menos el mas bajo'''
    jugador_menor_key = 0
    contador = 0
    bandera = True
    for jugador in lista_jugador:
        if jugador['estadisticas']['puntos_totales'] < jugador_menor_key or bandera == True:
            bandera = False
            jugador_menor_key = jugador['estadisticas']['puntos_totales']
    acumulador = 0
    for jugador in lista_jugador:
        puntos = jugador['estadisticas']['puntos_totales']
        acumulador += puntos
        contador = contador + 1
    calculo = acumulador - jugador_menor_key 
    promedio = calculo / contador
    print("Promedio de puntos totales del Dream team")
    print("Promedio total con todos los integrantes: ",acumulador / contador)
    print("Promedio excluyendo al jugador con menos puntos totales del Team: ", promedio)

def recorrer_y_mostrar_key(lista_jugador,key,promedio):
    '''Recibe la lista de jugadores, la clave a evaluar y el promedio ingresado por el usuario
    -Compara si el jugador supera el promedio ingresado
    -Devuelve el nombre, posicion y promedio del jugador si se supera el promedio'''
    flag = True
    for jugadores in lista_jugador:
        if jugadores['posicion'] == key and jugadores['estadisticas']['porcentaje_tiros_de_campo'] >promedio:
            flag = False
            print("------------------------------------------------------------------")
            print("Nombre: {0}\nPosicion: {1}\nSupera el promedio con: {2}".format(jugadores['nombre'],jugadores['posicion'],jugadores['estadisticas']['porcentaje_tiros_de_campo']))
            print("------------------------------------------------------------------")
    if flag:
        print("El ",key," no supera el primedio")

def calcular_mostrar_mayor_promedio(lista_jugador:list,key:str):
    '''Recibe la lista de jugadores y la clave a evaluar
    -Calcula si la clave que se evalua supera el promedio ingresado
    -Devuelve el nombre y el promedio, en caso contrario devuelve un mensaje'''
    print("------------------------------------------------------------------")
    promedio_ingresado = input("Ingrese un promedio y se mostrara que jugador supera el mismo: ")
    promedio_ingresado = float(promedio_ingresado)
    flag_promedio2 = 0
    for promedio in lista_jugador:
        if promedio_ingresado < promedio['estadisticas'][key]:
            flag_promedio2 = 1
            print("------------------------------------------------------------------")
            print("Nombre: {0}\nSupera el promedio ingresado con: {1}".format(promedio['nombre'],promedio['estadisticas'][key]))
            print("------------------------------------------------------------------")
    if flag_promedio2 == 0:
        print("El promedio ingresado es muy alto.")
        print("------------------------------------------------------------------")

def calcular_mostrar(lista_jugador,key,opcion):
    '''Recibe la lista de los jugadores, la key donde se va a calcular el mayor numero y la opcion del menu
    -Calcula que numero es mas grande y lo guarda junto a su nombre
    (La "opcion" es para el mensaje que se va a cargar dependiendo de la opcion que se ingrese)
    -Muestra por terminal la categoria y el nombre del jugador mas destacado'''
    jugador_mayor_key = 0
    nombre_jugador_mayor_key = None
    if opcion == 7:
        mensaje = "Rebotes totales" 
    elif opcion == 8:
        mensaje = "Porcentaje de tiros de campo"
    elif opcion == 9:
        mensaje = "Asistencias totales"
    elif opcion == 13:
        mensaje = "Robos totales"
    elif opcion == 14:
        mensaje = "Bloqueos totales"
    elif opcion == 19:
        mensaje = "Temporadas"
    for jugador in lista_jugador:
        if jugador['estadisticas'][key] > jugador_mayor_key:
            jugador_mayor_key = jugador['estadisticas'][key]
            nombre_jugador_mayor_key = jugador['nombre']
    print("------------------------------------------------------------------")
    print("{0}\nNombre: {1}\n{2}: {3}".format(mensaje,nombre_jugador_mayor_key,mensaje,jugador_mayor_key))
    print("------------------------------------------------------------------")

def lista_key(lista_jugador:list,key:str)->list:
    '''Recibe una lista del archivo json
        crea una lista vacia, recorre un For mientras agrega lo que indique la key a la lista
        devuelve la lista '''
    categoria = []
    for jugador in lista_jugador:
        categoria.append(jugador[key])   
    return categoria

def ordenar_por_key(lista_jugador:list,key_ordenar:str):
    '''Recibe una lista y la key de la categoria a ordenar
        pregunta si sera de manera ascendente o descendente el ordenamiento
        devuelve la categoria ordenada'''
    categoria = lista_key(lista_jugador,key_ordenar)

    rango_a = len(categoria)    
    for i in range(rango_a):
        for j in range(rango_a):
            if( categoria[i] < categoria[j] ):
                categoria[i],categoria[j] = categoria[j],categoria[i] 
    print("jugadores ordenados por",key_ordenar,": ")             
    for something in categoria:
        print("Nombre: ",something)
        print("-----------------------------------------------")

def capitalizar_palabras(cadena:str):
    '''Recibe una cadena de texto
    - Capitaliza las palabras ingresadas
    -Devuelve las palabras capitalizadas'''
    palabras = cadena.split()
    capitalizadas = []

    for palabra in palabras:
        capitalizada = palabra.capitalize()
        capitalizadas.append(capitalizada)

    cadena_capitalizada = " ".join(capitalizadas)
    
    return cadena_capitalizada

def buscar_jugadores_por_nombre(lista_jugador):
    '''Recibe la lista de jugadores
    -Evalua que se ingresen letras solamente y luego las capitaliza
    -Si las primeras 4 letras coinciden con el nombre de un jugador, devuelve el nombre que coincide'''
    nombres = []
    indice = None
    for jugadores in lista_jugador:
        nombres.append(jugadores['nombre'])
    jugador_buscar = input("Ingrese el nombre del jugador: ")
    validar_opcion = re.search(r"^([a-zA-Z]+)",jugador_buscar)
    jugador_buscar = capitalizar_palabras(jugador_buscar)
    if(validar_opcion_vacia(jugador_buscar) == False or validar_opcion == None):
        print("La opcion ingresada no es valida")
    else:
        for nombre in nombres:
            if(jugador_buscar[:4] == nombre[:4]):
                print(nombre)
                indice = nombres.index(nombre) + 1
                print("Indice: ",indice)
        return indice


def mostrar_logros_jugador(lista_jugador,indice):
    '''Recibe la lista de los jugadores y un indice
    Recore la lista solamente la parte que el indice le indica 
    Devuelve el nombre y los logros del jugador que se encuentra en el indice'''
    for jugador in lista_jugador[indice - 1:indice]:
        print("------------------------------------------------------------------")
        print("Nombre: ",jugador['nombre'])
        cadena = (jugador['logros'])
        logros = "\n         ".join(cadena)
        print("Logros: ",logros)
        print("------------------------------------------------------------------")
        
    
def buscar_jugador_por_id(lista_jugador):
    '''Recibe la lista de jugadores
    -Muestra una lista con el id y el nombre del jugador a un lado
    -Devuelve el numero de id del jugador'''
    mostrar_id_jugador(lista_jugador)
    jugador_elegido = input("\nIngrese el indice del jugador que desee: ")
    return jugador_elegido


def normalizar_datos(lista_jugador: list):
    '''Recibe la lista de jugadores
    -Verifica que la lista no este vacia, luego normaliza los datos flotantes a str
    -Devuelve todos los datos en str'''
    if len(lista_jugador) == 0:
        print("La lista está vacia")
    else:
        flag_datos_normalizado = False
        for clave in lista_jugador:
            clave["promedio_puntos_por_partido"] = str(clave["promedio_puntos_por_partido"])
            clave["promedio_rebotes_por_partido"] = str(clave["promedio_rebotes_por_partido"])
            clave["promedio_asistencias_por_partido"] = str(clave["promedio_asistencias_por_partido"])
            clave["porcentaje_tiros_libres"] = str(clave["porcentaje_tiros_libres"])
            clave["porcentaje_tiros_triples"] = str(clave["porcentaje_tiros_triples"])
            clave["porcentaje_tiros_de_campo"] = str(clave["porcentaje_tiros_de_campo"])
            clave["temporadas"] = str(clave["temporadas"])
            clave["puntos_totales"] = str(clave["puntos_totales"])
            clave["rebotes_totales"] = str(clave["rebotes_totales"])
            clave["asistencias_totales"] = str(clave["asistencias_totales"])
            clave["robos_totales"] = str(clave["robos_totales"])
            clave["bloqueos_totales"] = str(clave["bloqueos_totales"])

            flag_datos_normalizado = True

        if flag_datos_normalizado == True:
            print("Datos normalizados")

def leer_archivo(nombre_archivo:str)->dict:
    with open(nombre_archivo, 'r') as file:
        lista_jugadores = json.load(file)
        return lista_jugadores['jugadores']

def guardar_archivo_jugador(jugador:list):
    '''Recibe la lista deñ jugador a guardar
    -Crea un archivo "csv" y guarda los datos del jugador
    -No devuelve nada'''
    with open("jugador_archivo.csv", "w") as file:
        for elemento in jugador:
            file.write("Nombre: {0}\nPosicion: {1}\nTemporada: {2}\nPuntos totales: {3}\nPromedio de puntos por partido: {4}\nRebotes totales: {5}\nPromedio de rebotes por partido: {6}\nAsistencias totales: {7}\nPorcentaje de tiro de campo: {8}\nPorcentaje de tiros libres: {9}\nPorcentaje de tiros triples: {10}\n".format(elemento['nombre'],elemento['posicion'],elemento['estadisticas']['temporadas']
            ,elemento['estadisticas']['puntos_totales'],elemento['estadisticas']['promedio_puntos_por_partido'],elemento['estadisticas']['rebotes_totales']
            ,elemento['estadisticas']['promedio_rebotes_por_partido'],elemento['estadisticas']['asistencias_totales'],elemento['estadisticas']['porcentaje_tiros_de_campo']
            ,elemento['estadisticas']['porcentaje_tiros_libres'],elemento['estadisticas']['porcentaje_tiros_triples']))


def mostrar_jugadores(lista_jugadores):
    '''Recibe una lista de jugadores a procesar
    recorre la lista y muestra todos los jugadores'''
    for jugador in lista_jugadores:
        print("Nombre: {0}\nPosicion: {1}\n".format(jugador['nombre'],jugador['posicion']))

def validar_opcion_vacia(opcion):
    '''Recibe una opcion recibida por input
        Se comprueba que la opcion no este vacia
        Devuelve false si no tiene nada, en caso contrario devuelve true'''
    if len(opcion) <= 0:
        return False
    return True

def mostrar_id_jugador(lista_jugadores):
    '''Recibe la lista de jugadores
    crea un indice autoincremental que aumenta por cada vuelta del For
    muestra los nombres de los jugadores y su indice '''
    indice = 0
    for jugador in lista_jugadores:
        indice +=1
        print("Indice: {0}  | |  Nombre: {1}".format(indice,jugador['nombre']))

def estadisticas_jugador(lista_jugadores:list, indice):
    '''Recibe una lista de un jugador y su indice
    crea una lista de ese jugador y guarda sus estadisticas
    devuelve la lista con estadisticas'''
    estadisticas = []
    for jugador in lista_jugadores[indice - 1 :indice]:
        estadisticas.append(jugador['estadisticas'])
    return estadisticas    

       
def mostrar_estadisticas_jugador(lista_jugadores:list, key:str):
    '''Recibe la lista de estadisticas y la Key a mostrar
    recorre un for mostrando la estadistica de la key que se indico
    devuelve una estadistica indicada'''
    for estadisticas in lista_jugadores:
        print(estadisticas[key]) 

def mostrar_todas_estadisticas(lista_jugadores,lista_estadisticas, indice):
    '''En la primer lista recibe la lista de jugadores y en la segunda lista recibe las estadisticas
      de dicho jugador seleccionado por ID
      recorre un for mostrando el nombre y todas las estadisticas del jugador seleccionador por ID'''
    for jugador in lista_jugadores[indice - 1:indice]:
        print("------------------------------------------------------------------")
        print("Nombre: ",jugador['nombre'])
        print("Temporadas: ",end= "")
        mostrar_estadisticas_jugador(lista_estadisticas,'temporadas')
        print("Puntos totales: ",end="")
        mostrar_estadisticas_jugador(lista_estadisticas,'puntos_totales')
        print("Promedio de puntos por partido: ",end="")
        mostrar_estadisticas_jugador(lista_estadisticas,'promedio_puntos_por_partido')
        print("Rebotes totales: ",end="")
        mostrar_estadisticas_jugador(lista_estadisticas,'rebotes_totales')
        print("Promedio de rebotes por partido: ",end="")
        mostrar_estadisticas_jugador(lista_estadisticas,'promedio_rebotes_por_partido')
        print("Asistencias totales: ",end="")
        mostrar_estadisticas_jugador(lista_estadisticas,'asistencias_totales')
        print("Promedio de asistencias por partido: ",end="")
        mostrar_estadisticas_jugador(lista_estadisticas,'promedio_asistencias_por_partido')
        print("Robos totales: ",end="")
        mostrar_estadisticas_jugador(lista_estadisticas,'robos_totales')
        print("Bloqueos totales: ",end="")
        mostrar_estadisticas_jugador(lista_estadisticas,'bloqueos_totales')
        print("Porcentaje de tiros de campo: ",end="")
        mostrar_estadisticas_jugador(lista_estadisticas,'porcentaje_tiros_de_campo')
        print("Porcentaje de tiros libres: ",end="")
        mostrar_estadisticas_jugador(lista_estadisticas,'porcentaje_tiros_libres')
        print("Porcentaje de tiros triples: ",end="")
        mostrar_estadisticas_jugador(lista_estadisticas,'porcentaje_tiros_triples')
        print("------------------------------------------------------------------")
        jugador_guardado = lista_jugadores[indice - 1 : indice]
        return jugador_guardado


def imprimir_menu():
    '''imprime un menu no interactuable'''
    print("--------Menu de opciones---------")
    print("1.Mostrar la lista de todos los jugadores del Dream Team.")
    print("2.Seleccionar un jugador por su índice y mostrar sus estadísticas ")
    print("3.Guardar las estadísticas de ese jugador en un archivo CSV.")
    print("4.buscar un jugador por su nombre y mostrar sus logros")
    print("5.Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team")
    print("6.ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.")
    print("7.Calcular y mostrar el jugador con la mayor cantidad de rebotes totales")
    print("8.Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.")
    print("9.Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.")
    print("10.ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor")
    print("11.ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.")
    print("12.ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.")
    print("13.Calcular y mostrar el jugador con la mayor cantidad de robos totales.")
    print("14.Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales")
    print("15.ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.")
    print("16.Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.")
    print("17.Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos")
    print("18.ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.")
    print("19.Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas")
    print("20.Mostrar jugadores ordenados por posicion que tengan porcentaje de tiros de campo superior al calor ingresado.")
    print("0.Salida")


def menu_opcion():
    '''Le pide al usuario una opcion del menu impreso al comienzo de la funcion
        devuelve la opcion elegida o "-1" si la opcion no es valida'''
    imprimir_menu()
    opcion_elegida = input("Ingrese una opcion: ")
    validar_opcion = re.match(r"([0-9])",opcion_elegida)
    if(validar_opcion == None or len(opcion_elegida) <= 0):
        respuesta = "-1"
        return respuesta
    
    opcion_elegida = int(opcion_elegida)
    if(opcion_elegida > 20):
        respuesta = "-1"
    else:
        respuesta = opcion_elegida

    return respuesta

def menu_principal(lista_jugadores:list):
    flag_opcion2 = False
    opcion = None
    while(opcion != '0'):
        opcion = menu_opcion()
        if(opcion == 1):
            print("--------Ingreso a la opcion 1--------")
            mostrar_jugadores(lista_jugadores)
            pass
        elif(opcion == 2):
            print("--------Ingreso a la opcion 2--------")
            jugador_elegido = buscar_jugador_por_id(lista_jugadores)
            if(validar_opcion_vacia(jugador_elegido) == False):
                print("La opcion ingresada no es valida")
            else:
                jugador_elegido = int(jugador_elegido)
                estadisticas = estadisticas_jugador(lista_jugadores, jugador_elegido)
                if(jugador_elegido > 12 ):
                    print("El jugador que busca no existe")
                else:
                    jugador_guardado = mostrar_todas_estadisticas(lista_jugadores,estadisticas,jugador_elegido)
                    flag_opcion2 = True
            pass
        elif(opcion == 3):
            print("------Ingreso a la opcion 3--------")
            if flag_opcion2 == True:
                normalizar_datos(estadisticas)
                guardar_archivo_jugador(jugador_guardado)
                print("--------Se guardo correctamente!---------")
            else:
                print("Para ingresar a esta opcion debes primero ingresar a la 'Opcion 2'")
            
            print("-----------------------")
        elif(opcion == 4):
            print("------Ingreso a la opcion 4--------")
            indice = buscar_jugadores_por_nombre(lista_jugadores)
            if indice != None:
                mostrar_logros_jugador(lista_jugadores,indice)
            else:
                print("No se encontro el jugador.")
            pass
        elif(opcion == 5):
            print("------Ingreso a la opcion 5--------") 
            ordenar_por_key(lista_jugadores,'nombre')
            pass
        elif(opcion == 6):
            print("------Ingreso a la opcion 6--------")
            indice = buscar_jugadores_por_nombre(lista_jugadores)
            if indice != None:
                verificar_miembro_salon_de_la_fama(lista_jugadores,indice)
            else:
                print("No se encontro el jugador.")
            pass
        elif(opcion == 7):
            print("------Ingreso a la opcion 7--------")
            calcular_mostrar(lista_jugadores,'rebotes_totales',opcion)
            pass
        elif(opcion == 8):
            print("------Ingreso a la opcion 8--------")
            calcular_mostrar(lista_jugadores,'porcentaje_tiros_de_campo',opcion)
            pass
        elif(opcion == 9):
            print("------Ingreso a la opcion 9--------")
            calcular_mostrar(lista_jugadores,'asistencias_totales',opcion)
            pass
        elif(opcion == 10):
            print("------Ingreso a la opcion 10--------")
            calcular_mostrar_mayor_promedio(lista_jugadores,'promedio_puntos_por_partido')         
            pass
        elif(opcion == 11):
            print("------Ingreso a la opcion 11--------")
            calcular_mostrar_mayor_promedio(lista_jugadores,'promedio_rebotes_por_partido') 
            pass
        elif(opcion == 12):
            print("------Ingreso a la opcion 12--------")
            calcular_mostrar_mayor_promedio(lista_jugadores,'promedio_asistencias_por_partido') 
            pass
        elif(opcion == 13):
            print("------Ingreso a la opcion 13--------")
            calcular_mostrar(lista_jugadores,'robos_totales',opcion)
            pass
        elif(opcion == 14):
            print("------Ingreso a la opcion 14--------")
            calcular_mostrar(lista_jugadores,'bloqueos_totales',opcion)
            pass
        elif(opcion == 15):
            print("------Ingreso a la opcion 15--------")
            calcular_mostrar_mayor_promedio(lista_jugadores,'porcentaje_tiros_libres') 
            pass
        elif(opcion == 16):
            print("------Ingreso a la opcion 16--------")
            calcular_mostrar_menor_promedio(lista_jugadores)
            pass
        elif(opcion == 17):
            print("------Ingreso a la opcion 17--------")
            calcular_mostrar_jugador_mas_logros(lista_jugadores)
            pass
        elif(opcion == 18):
            print("------Ingreso a la opcion 18--------")
            calcular_mostrar_mayor_promedio(lista_jugadores,'porcentaje_tiros_triples') 
            pass
        elif(opcion == 19):
            print("------Ingreso a la opcion 19--------")
            calcular_mostrar(lista_jugadores,'temporadas',opcion)
            pass
        elif(opcion == 20):
            print("------Ingreso a la opcion 20--------")
            print("------------------------------------------------------------------")
            promedio_ingresado = input("Ingrese un promedio y se mostrara que jugador supera el mismo: ")
            promedio_ingresado = float(promedio_ingresado)
            recorrer_y_mostrar_key(lista_jugadores,'Base',promedio_ingresado)
            recorrer_y_mostrar_key(lista_jugadores,'Escolta',promedio_ingresado)
            recorrer_y_mostrar_key(lista_jugadores,'Alero',promedio_ingresado)
            recorrer_y_mostrar_key(lista_jugadores,'Ala-Pivot',promedio_ingresado)
            recorrer_y_mostrar_key(lista_jugadores,'Pivot',promedio_ingresado)   
            pass
        elif(opcion == 0):
            print("--------Saliste del menu----------")
            break
        elif(opcion == '-1'):
            print("se ingreso una opcion invalida, intente de nuevo")

def main():
    '''En esta funcion se encuentra todo el contenido'''
    lista_jugadores = leer_archivo('E:\Programacion-1\primer_Parcial\dt.json')
    menu_principal(lista_jugadores) 

main()

