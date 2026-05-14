#Las librerias, df =dataframe pd pandas
#Yo añadi tabulate y colorama para el diseño estetico
import pandas as pd
from tabulate import tabulate
from colorama import init, Fore

init(autoreset=True)


df = pd.read_excel("cuerpos_celestes2.xlsx")
cuerpos = df.to_dict(orient="records")

#funcion para titulo
def titulo():

    print(Fore.CYAN + r"""
   █████╗ ███████╗████████╗██████╗  ██████╗ 
  ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗
  ███████║███████╗   ██║   ██████╔╝██║   ██║
  ██╔══██║╚════██║   ██║   ██╔══██╗██║   ██║
  ██║  ██║███████║   ██║   ██║  ██║╚██████╔╝
  ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝
    """)

    print(Fore.YELLOW + "🌌 SISTEMA ASTRONÓMICO 🌌")
    print(Fore.BLUE + "=" * 50)

#funcion para el menú principal
def menu():

    print(Fore.MAGENTA + """
╔════════════════════════════════════╗
║         MENÚ PRINCIPAL            ║
╠════════════════════════════════════╣
║ 1️⃣  Ver todos los cuerpos         ║
║ 2️⃣  Buscar por tipo               ║
║ 3️⃣  Agregar cuerpo celeste        ║
║ 4️⃣  Guardar y salir               ║
╚════════════════════════════════════╝
""")

#funcion para validar el texto que ingrese el usuario :)
def pedir_texto(mensaje):

    while True:

        dato = input(mensaje).strip()

        if dato == "":
            print(Fore.RED + "❌ No puede estar vacío.")
        else:
            return dato
        
#funcion para validar que los datos que sean números sean validos y positivos
def pedir_numero(mensaje):

    while True:

        try:
            numero = float(input(mensaje))

            if numero <= 0:
                print(Fore.RED + "❌ Debe ser mayor que 0.")

            else:
                return numero

        except ValueError:
            print(Fore.RED + "❌ Ingresa un número válido.")

#funcion para que el usuario vea todos los datos almacenados de la base
def ver_datos():

    if len(cuerpos) == 0:
        print(Fore.RED + "\n⚠ No hay cuerpos registrados.\n")
        return

    print(Fore.CYAN + "\n🌠 LISTA DE CUERPOS CELESTES 🌠\n")

    print(tabulate(
        cuerpos,
        headers="keys",
        tablefmt="fancy_grid",
        showindex=True
    ))

#funcion para cuando el usuario quiera buscar un cuerpo por tipo
def buscar_tipo():

    tipo = pedir_texto("\n🔎 Tipo a buscar: ")

    encontrados = []

    for c in cuerpos:

        if c["tipo"].lower() == tipo.lower():
            encontrados.append(c)

    if encontrados:

        print(Fore.GREEN + "\n✅ RESULTADOS ENCONTRADOS:\n")

        print(tabulate(
            encontrados,
            headers="keys",
            tablefmt="fancy_grid",
            showindex=False
        ))

    else:
        print(Fore.RED + "\n❌ No se encontraron resultados.")


#funcion para agregar un cuerpo, aqui se aplican algunas funciones que escribi anteriormente como pedir_texto
# y pedir_numero, esto para validar el texto y los numeros que ingrese el usuario
def agregar_cuerpo():

    print(Fore.YELLOW + "\n🌌 AGREGAR NUEVO CUERPO CELESTE\n")

    nuevo = {

        "nombre": pedir_texto("Nombre: "),

        "tipo": pedir_texto("Tipo: "),

        "ubicacion": pedir_texto("Ubicación: "),

        "distancia": pedir_numero("Distancia: "),

        "diametro": pedir_numero("Diámetro: ")
    }

    cuerpos.append(nuevo)

    print(Fore.GREEN + "\n✅ Cuerpo agregado correctamente.")


#funcion para la opcion guardar y salir
def guardar():

    try:

        df = pd.DataFrame(cuerpos)

        df.to_excel("cuerpos_celestes.xlsx", index=False)

        print(Fore.GREEN + "\n💾 Datos guardados correctamente.")

    except Exception as e:

        print(Fore.RED + f"\n❌ Error al guardar: {e}")


# PROGRAMA PRINCIPAL

while True:

    titulo()
    menu()

    opcion = input(Fore.CYAN + "👉 Opción: ")

    # VER DATOS
    if opcion == "1":

        ver_datos()

    # BUSCAR
    elif opcion == "2":

        buscar_tipo()

    # AGREGAR
    elif opcion == "3":

        agregar_cuerpo()

    # GUARDAR Y SALIR
    elif opcion == "4":

        guardar()

        print(Fore.CYAN + "\n🚀 Cerrando sistema astronómico...\n")

        break

    # OPCIÓN INVÁLIDA
    else:

        print(Fore.RED + "\n❌ Opción inválida.")

    input(Fore.YELLOW + "\nPresiona ENTER para continuar...")

'''
#ESTE ES EL MENU, SI TIENEN MAS IDEAS DEL MENU PODEMOS AGREGARLAS
#while True: 
    print("\n1. Ver datos")
    print("2. Buscar por tipo")
    print("3. Agregar")
    print("4. Guardar y salir")

    opcion = input("Opción: ")

#AQUI FALTA AGREGAR COSAS, AGREGAR VARIABBLES , ADEMAS DE CUERPOS
#QUIZA PODRIAMOS USAR FUNCIONES
    if opcion == "1":
        for c in cuerpos:
            print(c)

    elif opcion == "2":
        tipo = input("Tipo: ")
        for c in cuerpos:
            if c["tipo"].lower() == tipo.lower():
                print(c)

    elif opcion == "3":
        nuevo = {
            "nombre": input("Nombre: "),
            "tipo": input("Tipo: "),
            "ubicacion": input("Ubicación: "),
            "distancia": float(input("Distancia: ")),
            "diametro": float(input("Diámetro: "))
        }
        cuerpos.append(nuevo)

    elif opcion == "4":
        df = pd.DataFrame(cuerpos)
        df.to_excel("cuerpos_celestes.xlsx", index=False)
        print("Guardado.")
        break

    else:
        print("Opción inválida")'''
