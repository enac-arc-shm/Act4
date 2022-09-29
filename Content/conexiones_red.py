import dispositivos_red as dispositivos_red
import dispositivos_finales as dispositivos_finales

conexiones = []

def conexiones():
    global conexiones
    red = dispositivos_red.get_dispositivos_de_red()
    final = dispositivos_finales.get_dispositivos_finales()

    dispred = input("Ingresa el dispositivo de red: ")

    if dispred in red:

        dispfinal = input("Ingresa el dispositivo final :")

        if dispfinal in final:
            conexiones.append(f"[+]{dispred}->{dispfinal}")
            print (f"[+]{dispred}->{dispfinal}")

        else:
            print("No se encontro el dispositivo final")

    else:
        print("No se encontro el dispositivo de red")