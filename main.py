from calendar import c
from traceback import print_tb
import easygui as eg
from os import system
system("cls")

archivoData = ''
archivoInstrucciones = ''
mes = ''
year = ''
datos = []

def menuprincipal():
    print("Opciones: \n1.Cargar data \n2.Cargar instrucciones \n3.Analizar \n4.Reportes \n5.Salir")
    print('--------------------------------------------------')
    lectura = input("Escoja una opcion: ")
    print('--------------------------------------------------')
    if int(lectura) == 1:
        cargarData()
        menuprincipal()
    elif int(lectura) == 2:
        cargarInstrucciones()
        menuprincipal()
        '''notayposicion = usar.Obtenernotas()
        for i in range(len(notayposicion)):
            print(usar.MostrarAscendente(notayposicion[i][1]))
        ejecutar(listaParametros)
        menuprincipal()'''
    elif int(lectura) == 3:
        analizar()
        menuprincipal()
    elif int(lectura) == 4:
        #reportes()
        print("reportes")
        menuprincipal()
    elif int(lectura) == 5:
        exit()
    else:
        print("No es una opcion valida")
        menuprincipal()

def cargarData():
    global archivoData
    extension = ["*.py","*.pyc"]
    archivo = eg.fileopenbox(msg="Abrir archivo",
                         title="Control: fileopenbox",
                         default='C:/Users/USUARIO/Desktop/*data',
                         filetypes=extension)                      
    eg.msgbox(archivo, "fileopenbox", ok_button="Continuar")
    f = open(archivo,'r',encoding="utf8")
    leer = f.read()
    f.close()
    archivoData = leer.replace("\n","")
    imprimir = '*********************************************'
    imprimir1 = 'Archivo Cargado exitosamente'
    print(imprimir.center(50,' ') + '\n' + imprimir1.center(50,' ') + '\n' + imprimir.center(50,' ') + '\n')
    menuprincipal()

def cargarInstrucciones():
    global archivoInstrucciones
    extension = ["*.py","*.pyc"]
    archivo = eg.fileopenbox(msg="Abrir archivo",
                         title="Control: fileopenbox",
                         default='C:/Users/USUARIO/Desktop/*lfp',
                         filetypes=extension)                      
    eg.msgbox(archivo, "fileopenbox", ok_button="Continuar")
    f = open(archivo,'r',encoding="utf8")
    leer = f.read()
    f.close()
    archivoInstrucciones = leer.replace("\n","")
    imprimir = '*********************************************'
    imprimir1 = 'Archivo Cargado exitosamente'
    print(imprimir.center(50,' ') + '\n' + imprimir1.center(50,' ') + '\n' + imprimir.center(50,' ') + '\n')
    menuprincipal()

def analizar():
    global archivoData,archivoInstrucciones
    archivoData = archivoData + "#"
    archivoInstrucciones = archivoInstrucciones + '@'
    print(archivoData)
    print(archivoInstrucciones)
    analizarData()
    print(datos[0][0])
    exit()

def analizarData():
    global archivoData,archivoInstrucciones,mes,year,datos
    print('AnalizarData')
    contador = 0
    state = 0
    temp = ''
    while (int(contador) <= int(len(archivoData))):
        if state == 0:
            if archivoData[contador] == '#':
                break
            elif archivoData[contador].isalpha():
                temp += archivoData[contador]
                contador += 1
            elif archivoData[contador] == ':':
                mes = temp
                temp = ''
                contador += 1
            elif archivoData[contador] == " ":
                contador += 1
            elif archivoData[contador].isnumeric():
                temp += archivoData[contador]
                contador += 1
            elif archivoData[contador] == '=':
                year = temp
                temp = ''
                contador += 1
                state = 1
        elif state == 1:
            if archivoData[contador] == '(':
                contador += 1
            elif archivoData[contador] == ' ':
                contador += 1
            elif archivoData[contador] == '[':
                contador += 1 
            elif archivoData[contador] == '"' or archivoData[contador] == '“' or archivoData[contador] == '”':
                contador += 1
            elif archivoData[contador].isalpha():
                temp += archivoData[contador]
                contador += 1
            elif archivoData[contador] == ',' or archivoData[contador] == ',':
                temp += archivoData[contador]
                contador += 1
            elif archivoData[contador].isnumeric():
                temp += archivoData[contador]
                contador += 1
            elif archivoData[contador] == '.':
                temp += archivoData[contador]
                contador += 1
            elif archivoData[contador] == ']':
                temporal = temp.split(',')
                if temporal[2] != '':
                    datos.append(temporal)
                    temp = ''
                else:
                    temp = ''
                contador += 1
            elif archivoData[contador] == ';':
                contador += 1
            elif archivoData[contador] == ')':
                print(datos)
                contador += 1
                state = 0
                


menuprincipal()