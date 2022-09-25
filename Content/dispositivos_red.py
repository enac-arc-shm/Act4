#Importar clases 
import imprimir
import interfaces

dispositivos_de_red = {}

def set_dispositivos_de_red(key, valor):
    global dispositivos_de_red
    dispositivos_de_red[key] = valor

def get_dispositivos_de_red():
    global dispositivos_de_red
    return dispositivos_de_red

def crear_dispositivo(nombre, interfaces):
    set_dispositivos_de_red(nombre, interfaces)

def eliminar_dispositivo(key):
    dispositivos_de_red = get_dispositivos_de_red()
    if key in dispositivos_de_red:
        dispositivos_de_red.pop(key)
        imprimir.imprimir_mensaje_eliminar()
    else:
        imprimir.imprimir_mensaje_eliminar_error()