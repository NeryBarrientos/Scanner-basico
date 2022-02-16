import easygui as eg
import webbrowser
from os import system
system("cls")

archivoData = ''
archivoInstrucciones = ''
mes = ''
year = ''
datos = []
datos1 = []

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
    elif int(lectura) == 3:
        analizar()
        menuprincipal()
    elif int(lectura) == 4:
        reportes()
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
    #print(archivoData)
    #print(archivoInstrucciones)
    analizarData()
    analizarInstrucciones()
    imprimir = '*********************************************'
    imprimir1 = 'Archivo analizado exitosamente'
    print(imprimir.center(50,' ') + '\n' + imprimir1.center(50,' ') + '\n' + imprimir.center(50,' ') + '\n')
    #print(datos)
    #print(datos1)
    menuprincipal()

def analizarData():
    global archivoData,archivoInstrucciones,mes,year,datos
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
                if temporal[2] != '' and temporal[1] != '' and temporal[0] != '':
                    #print(temporal)
                    datos.append(temporal)
                    temp = ''
                else:
                    temp = ''
                contador += 1
            elif archivoData[contador] == ';':
                contador += 1
            elif archivoData[contador] == ')':
                contador += 1
                state = 0
                
def analizarInstrucciones():
    global datos1
    contador = 0
    state = 0
    temp = ''
    while (int(contador) <= int(len(archivoInstrucciones))):
        if state == 0:
            if archivoInstrucciones[contador] == '@':
                break
            elif archivoInstrucciones[contador] == '<' or archivoInstrucciones[contador] == '¿' or archivoInstrucciones[contador] == ' ':
                contador += 1
            elif archivoInstrucciones[contador].isalpha():
                temp += archivoInstrucciones[contador]
                contador += 1
            elif archivoInstrucciones[contador] == ':':
                temp += archivoInstrucciones[contador]
                contador += 1
            elif archivoInstrucciones[contador] == '"':
                state = 1
                contador += 1
        elif state == 1:
            if archivoInstrucciones[contador].isalpha() or archivoInstrucciones[contador].isnumeric() or archivoInstrucciones[contador] == ' ':
                temp += archivoInstrucciones[contador]
                contador += 1
            elif archivoInstrucciones[contador] == '"':
                contador += 1
            elif archivoInstrucciones[contador] == ',':
                contador += 1
                temporal = temp.split(':')
                datos1.append(temporal)
                temp = ''
                state = 0
            elif archivoInstrucciones[contador] == '?':
                contador += 1
                temporal = temp.split(':')
                datos1.append(temporal)
                temp = ''
            elif archivoInstrucciones[contador] == '>':
                contador += 1
                state = 0

def MetodoBurbuja(Lista):
    for num in range(len(Lista)-1,0,-1):
        for i in range(num):
            if int(Lista[i][2])>int(Lista[i+1][2]):
                temporal = Lista[i]
                Lista[i] = Lista[i+1]
                Lista[i+1] = temporal
    return Lista

def MetodoBurbujaTabla(Lista):
    for num in range(len(Lista)-1,0,-1):
        for i in range(num):
            if float(float(Lista[i][2])*float(Lista[i][1]))<float(float(Lista[i+1][2])*float(Lista[i+1][1])):
                temporal = Lista[i]
                Lista[i] = Lista[i+1]
                Lista[i+1] = temporal
    return Lista

def reportes():
    html = '<!DOCTYPE html> \n<html lang="en"> \n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> \n<title>Reportes</title> \n<link rel="stylesheet" href="css/bootstrap.min.css">'
    html = html + '\n<style> \nbody { background-image: url("fondo.jpg");\nbackground-size: cover;}\n.container{ margin: 50px auto;\n   border: 5px solid #000;\n   width: 70%;} \n</style> \n</head> \n<body> \n'
    html += '<div class="container bg-primary"> \n<h1 class="text-center bg-info text-primary"><strong>a) Nery Barrientos 201807086</strong></h1>'
    prueba = MetodoBurbuja(datos)
    prueba1 = MetodoBurbujaTabla(datos)
    #print(prueba)
    html += '\n<h1 class="text-center bg-info text-primary"><strong>b) Tabla de Ganancias generadas</strong></h1>'
    html += '\n<table class="table table-bordered text-center">\n<thead>\n<tr class="info">\n<th class="text-center">Nombre</th>\n<th class="text-center">Precio</th>\n<th class="text-center">Vendido en el mes</th>\n<th class="text-center">Ganancias generadas</th>\n</tr>\n</thead>'
    for i in range(len(prueba1)):
        temporal = '\n<tr class="info">\n<th class="text-center">' + str(prueba1[i][0]) + '</th>\n<th class="text-center">'+ str(prueba1[i][1]) +'</th>\n<th class="text-center">' + str(prueba1[i][2]) + '</th>\n<th class="text-center">' + str(float(prueba1[i][1])*float(prueba1[i][2])) + '</th></tr>'
        html += temporal
    html += '\n</table>'
    html += '<h1 class="text-center bg-info text-primary"><strong>c) El producto mas vendido es: ' + str(prueba[0][0]) +' </strong></h1>'
    html += '<h1 class="text-center bg-info text-primary"><strong>d) El producto menos vendido es: ' + str(prueba[-1][0]) +' </strong></h1>'
    crear = open('reporte.html' , 'w',encoding="utf8")
    crear.write(html)
    crear.close()
    imprimir = '*********************************************'
    imprimir1 = 'Reporte Generado exitosamente'
    print(imprimir.center(50,' ') + '\n' + imprimir1.center(50,' ') + '\n' + imprimir.center(50,' ') + '\n')
    webbrowser.open_new_tab('reporte.html')


menuprincipal()