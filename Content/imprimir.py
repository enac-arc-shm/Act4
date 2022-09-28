def imprimir_error():
    print("[-]Error, dato incorrecto")

def imprimir_menu_inicio():
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

def imprimir_menu_dispositivosRed():
    print("------------------Seleccione un dispositivo  a realizar----------------")
    print("[1] Crear un Router")
    print("[2] Crear un Switch")
    print("[3] Crear un ISP")
    print("-----------------------------------------------------------------------")

def imprimir_dispositivos_de_red(diccionario_dispositivos_red):
    print("---------------------------------------------")
    print("         Lista de dispositivos de red        ")
    print("                                             ")
    for dispositivo, datos in diccionario_dispositivos_red.items():
        print(f" [+] Nombre del dispositivo: {dispositivo}")
        print("                                           ")

def imprimir_dispositivos_finales(diccionario_dispositivos_finales):
    print("---------------------------------------------")
    print("         Lista de dispositivos finales       ")
    print("                                             ")
    for dispositivo, datos in diccionario_dispositivos_finales.items():
        print(f" [+] Nombre del dispositivo: {dispositivo}")
        print("                                           ")

def imprimir_dispositivos_info(diccionario_dispositivos):
    for dispositivo, datos in diccionario_dispositivos.items():
        print("____________________________________________")
        print(f"Nombre del dispositivo: {dispositivo}")
        print("--------------------------------------------")
        print("        Puerto     | Información del puerto ")
        for puerto, info in datos.items():
            print(f"{puerto}................{info}")
        print("                                            ")
        print("                                            ")
        
def imprimir_mensaje_eliminar():
    print(" [-] Elemento eliminado correctamente")

def imprimir_mensaje_eliminar_error():
    print(" [!] Elemento no encontrado")