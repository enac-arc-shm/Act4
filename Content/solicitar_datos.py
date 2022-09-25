#Clase para solicitar datos:
from pickle import TRUE
import imprimir_mensajes
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def imprimir_menu_inicio():
    clearConsole()
    print("------------------Seleccione la acción a realizar----------------")
    print("[1] Crear dispositivo de red")
    print("[2] Crear dispositivo final")
    print("[3] eliminar dispositivo de red")
    print("[4] eliminar dispositivo final")
    print("[5] Crear conexión")
    print("[6] Crear VLANS en switch")
    print("[7] Agregar parametros de red")
    print("[8] Imprimir dispositivos de red")
    print("-----------------------------------------------------------------")
    while True:
        try:
            opcion = int(input("[?] Teclee una opción: "))
            if opcion > 0 and opcion < 9:
                break
            else: 
                imprimir_mensajes.imprimir_error()
        except ValueError:
            imprimir_mensajes.imprimir_error()
    return opcion

def imprimir_menu_dispositivosRed():
    clearConsole()
    print("------------------Seleccione un dispositivo  a realizar----------------")
    print("[1] Crear un Router")
    print("[2] Crear un Switch")
    print("[3] Crear un ISP")
    print("-----------------------------------------------------------------------")
    while True:
        try:
            opcion = int(input("[?] Teclee una opción: "))
            if opcion > 0 and opcion < 4:
                break
            else: 
                imprimir_mensajes.imprimir_error()
        except ValueError:
            imprimir_mensajes.imprimir_error()
    return opcion


def solicitar_nombre_dispositivo_red(_tipo_):
    nombre = input(f"Ingrese el nombre del dispositivo de red({_tipo_}): ")
    return nombre

def solicitar_nombre_dispositivo_final(_tipo_):
    nombre = input("Ingrese el nombre del dispositivo de red(): ")
    return nombre

def solicitar_tipo_dispositivo():
    print("")
    nombre = input("Ingrese el nombre del dispositivo de red: ")
    return nombre

def solicitar_puertosFa():
    while True:
        try:
            puertos = int(input("Ingrese el numero de puertos FastEthernet: "))
            break
        except ValueError:
            imprimir_mensajes.imprimir_error()
    return puertos

def solicitar_puertosGig():
    while True:
        try:
            puertos = int(input("Ingrese el numero de puertos GIgabiteEthernet: "))
            break
        except ValueError:
            imprimir_mensajes.imprimir_error()
    return puertos

def solicitar_puertosLoop():
    while True:
        try:
            puertos = int(input("Ingrese el numero de puertos Loopback: "))
            break
        except ValueError:
            imprimir_mensajes.imprimir_error()
    return puertos

def solicitar_puertosSerial():
    PuertosSeriales = []
    while True:
        try:
            puertos = int(input("Ingrese el numero de puertos Seriales: "))
            break
        except ValueError:
            imprimir_mensajes.imprimir_error()
    for puerto in range(1,puertos + 1):
        PuertosSeriales.append(input(f"Ingrese el nombre del puerto Serial {puerto}: "))
    return PuertosSeriales