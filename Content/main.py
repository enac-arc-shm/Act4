import dispositivos_red
import dispositivos_finales
import interfaces
import solicitar_datos

if __name__ == "__main__":
    while True:
        opcion = solicitar_datos.menu_inicio()
        if opcion == 1:
            dispositivo_red = solicitar_datos.menu_dispositivosRed()
            if dispositivo_red == 1:
                datos = interfaces.generar_interfaces_RT(solicitar_datos.solicitar_puertosGig(), solicitar_datos.solicitar_puertosSerial(), solicitar_datos.solicitar_puertosLoop())
                dispositivos_red.crear_dispositivo(solicitar_datos.solicitar_nombre_dispositivo_red("Router"), datos)
            if dispositivo_red == 2:
                datos = interfaces.generar_interfaces_sw(solicitar_datos.solicitar_puertosFa(),solicitar_datos.solicitar_puertosGig())
                dispositivos_red.crear_dispositivo(solicitar_datos.solicitar_nombre_dispositivo_red("Switch"), datos)
            if dispositivo_red == 3:
                datos = interfaces.generar_interfaces_ISP(solicitar_datos.solicitar_puertosSerial(), solicitar_datos.solicitar_puertosLoop())
                dispositivos_red.crear_dispositivo(solicitar_datos.solicitar_nombre_dispositivo_red("ISP"), datos)
        if opcion == 2:
            datos = interfaces.generar_interfaces_DispositivoFinal(solicitar_datos.solicitar_puertosFa())
            dispositivos_finales.crear_dispositivo_final(solicitar_datos.solicitar_nombre_dispositivo_final())

        if opcion == 3:
            


        if opcion == 8:
            solicitar_datos.clearConsole()
            print(dispositivos_red.get_dispositivos_de_red())
            pausa = input("Presione una tecla para continuar...")