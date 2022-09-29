import dispositivos_red
import imprimir
vlans = []
dispositivo_vlan={}

def solicitar():
    key = input("Ingrese el nombre del dispositivo: ")
    dispositivos_finales = dispositivos_red.get_dispositivos_de_red()

    if key in dispositivos_finales:
        nv = int(input("Ingrese el número de vlans: "))
        for nvlan in range(0, nv):
            nnv=input("Ingresa el número de vlan: ")
            ip = input("Ingresa la dirección ip de esta VLAN: ")
            ms = input("Ingresa la mascara de subred de esta VLAN: ")
            gw = input("Ingresa la gateway predeterminada: ")
            vlans.append(f"VLAN{nnv} - IP: {ip} - Mascara de subred: {ms} -")
        dispositivo_vlan[key]= vlans
        print(dispositivo_vlan)
    else:
        imprimir.imprimir_mensaje_eliminar_error()