


def generar_interfaces_sw(FastEthernet, GigabitEthernet):
    interfaces = {}
    for interfaz in range(1, FastEthernet):
        interfaces[f"Fa0/{interfaz}"] = "Disponible"
    for interfaz in range(1, GigabitEthernet):
        interfaces[f"G0/{interfaz}"] = "Disponible"
    return interfaces

def generar_interfaces_RT(GigabitEthernet, Serial, Loopback):
    interfaces = {}
    for interfaz in range(1, GigabitEthernet):
        interfaces[f"G0/{interfaz}"] = "Disponible"
    for interfaz in Serial:
        interfaces[interfaz] = "Disponible"
    for interfaz in range(1, Loopback):
        interfaces[f"Lo{interfaz}"] = "Disponible"
    return interfaces

def generar_interfaces_ISP(Serial, Loopback):
    interfaces = {}
    for interfaz in Serial:
        interfaces[interfaz] = "Disponible"
    for interfaz in range(1, Loopback):
        interfaces[f"Lo{interfaz}"] = "Disponible"
    return interfaces