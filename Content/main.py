import dispositivos_red
import interfaces
import solicitar_datos

if __name__ == "__main__":
    while True:
        opcion = solicitar_datos.imprimir_menu_inicio()
        if opcion == 1:
            dispositivo_red = opcion = solicitar_datos.imprimir_menu_dispositivosRed()
            if dispositivo_red == 1:
                datos = interfaces.generar_interfaces_RT(solicitar_datos.solicitar_puertosGig, solicitar_datos.solicitar_puertosSerial, solicitar_datos.solicitar_puertosLoop)
                dispositivos_red.crear_router(solicitar_datos.solicitar_nombre_dispositivo(), datos)
