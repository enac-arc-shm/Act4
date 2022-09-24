#Importar clases 
import solicitar_datos
import interfaces

dispositivos_de_red = {}

def set_dispositivos_de_red(key, valor):
    global dispositivos_de_red
    dispositivos_de_red[key] = valor

def get_dispositivos_de_red():
    global dispositivos_de_red
    return dispositivos_de_red

def crear_router(nombre, datos):
    global dispositivos_de_red
    set_dispositivos_de_red(nombre, datos)
    print(dispositivos_de_red)