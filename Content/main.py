import dispositivos_red as dispositivos_red
import dispositivos_finales as dispositivos_finales
import interfaces as interfaces
import solicitar_datos as solicitar_datos
import imprimir as imprimir

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
            dispositivos_finales.crear_dispositivo_final(solicitar_datos.solicitar_nombre_dispositivo_final(), datos)

        if opcion == 3:
            solicitar_datos.clearConsole()
            imprimir.imprimir_dispositivos_de_red(dispositivos_red.get_dispositivos_de_red())
            dipositivo_eliminar = solicitar_datos.solicitar_dispositivo_eliminar()
            dispositivos_red.eliminar_dispositivo(dipositivo_eliminar)
            pausa = input("Presione una tecla para continuar...")

        if opcion == 4:
            solicitar_datos.clearConsole()
            imprimir.imprimir_dispositivos_finales(dispositivos_finales.get_dispositivos_finales())
            dipositivo_eliminar = solicitar_datos.solicitar_dispositivo_eliminar()
            dispositivos_finales.eliminar_dispositivo(dipositivo_eliminar)
            pausa = input("Presione una tecla para continuar...")

        if opcion == 5:
            pausa = input("Presione una tecla para continuar...")
            #emilio 

        if opcion == 7:
            imprimir.imprimir_dispositivos_info(dispositivos_red.get_dispositivos_de_red())
            dispositivo = solicitar_datos.solicitar_dispositivos_parametros()
            interfaz = solicitar_datos.solicitar_dispositivos_interfaz()
            while dispositivos_red.verificar_informacion(dispositivo, interfaz):
                print ("[-] Dispositivo e interfaz encontrada ")
            
            pausa = input("Presione una tecla para continuar...")

        if opcion == 8:
            solicitar_datos.clearConsole()
            print(dispositivos_red.get_dispositivos_de_red())
            pausa = input("Presione una tecla para continuar...")
