import re  # Importa la biblioteca de expresiones regulares

# Función para cargar la lista negra desde un archivo externo
def cargar_blacklist():
    try:
        with open("blacklist.txt", "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print("El archivo 'blacklist.txt' no existe. La lista negra se mantendrá vacía.")
        return []

# Función para guardar la lista negra en el archivo externo
def guardar_blacklist():
    with open("blacklist.txt", "w") as file:
        for ip in blacklist:
            file.write(ip + "\n")


# Cargar la lista negra desde el archivo externo
blacklist = cargar_blacklist()

# Función para mostrar la lista negra
def mostrar_blacklist():
    print("Lista negra de direcciones IP:")
    for ip in blacklist:
        print(ip)


# Función para agregar una dirección IP a la lista negra
def agregar_a_blacklist(ip):
    # Utiliza una expresión regular para verificar si la cadena es una dirección IP válida
    if re.match(r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ip) and ip not in blacklist:
        blacklist.append(ip)
        print(f"La dirección IP {ip} ha sido agregada a la lista negra.")
    else:
        print("Dirección IP no válida o ya en la lista negra.")

# Función para eliminar una dirección IP de la lista negra
def eliminar_de_blacklist(ip):
    if ip in blacklist:
        blacklist.remove(ip)
        print(f"La dirección IP {ip} ha sido eliminada de la lista negra.")
    else:
        print(f"La dirección IP {ip} no se encuentra en la lista negra.")

# Función para filtrar un paquete basado en la lista negra
def filtrar_paquete(ip):
    if ip in blacklist:
        print(f"Paquete de {ip} bloqueado por el firewall.")
    else:
        print(f"Paquete de {ip} permitido por el firewall.")

# Bucle principal del programa
while True:
    print("\n-- Firewall Simple --")
    print("1. Mostrar lista negra")
    print("2. Agregar dirección IP a la lista negra")
    print("3. Eliminar dirección IP de la lista negra")
    print("4. Simular recepción de paquetes")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        mostrar_blacklist()
    elif opcion == "2":
        ip = input("Ingresa la dirección IP a agregar a la lista negra: ")
        agregar_a_blacklist(ip)
    elif opcion == "3":
        ip = input("Ingresa la dirección IP a eliminar de la lista negra: ")
        eliminar_de_blacklist(ip)
    elif opcion == "4":
        # Simulación de recepción de paquetes
        paquetes = ["192.168.1.1", "192.168.1.2", "10.0.0.1", "192.168.1.3", "192.168.1.4"]
        for paquete in paquetes:
            filtrar_paquete(paquete)
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")

guardar_blacklist()
