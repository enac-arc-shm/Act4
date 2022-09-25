#Importar clases 
import solicitar_datos
import interfaces

dispositivos_finales = {}

def set_dispositivos_finales(key, valor):
    global dispositivos_finales
    dispositivos_finales[key] = valor

def get_dispositivos_finales():
    global dispositivos_finales
    return dispositivos_finales

def crear_dispositivo_final(nombre, puertos):
    dispositivos_finales(nombre, puertos)

