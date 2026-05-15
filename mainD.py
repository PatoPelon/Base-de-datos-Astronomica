#Las librerias, df =dataframe pd pandas
#Yo añadi tabulate y colorama para el diseño estetico
import pandas as pd
from tabulate import tabulate
from colorama import init, Fore

init(autoreset=True)

import os

print(os.getcwd())
print(os.listdir())
df = pd.read_excel("cuerpos_celestes.xlsx")

# limpiar espacios en columnas
df.columns = df.columns.str.strip().str.lower()
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
║         MENÚ PRINCIPAL             ║
╠════════════════════════════════════╣
║ 1️  Ver todos los cuerpos           ║
║ 2️  Buscar por tipo                 ║
║ 3️  Agregar cuerpo celeste          ║
║ 4️  Eliminar cuerpo celeste         ║
║ 5️  Modificar datos                 ║
║ 6️  Buscar por inicial              ║
║ 7️  Guardar y salir                 ║
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

        if c.get("tipo", "").lower() == tipo.lower():
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

      "distancia (ly)": pedir_numero("Distancia: "),

      "diametro (km)": pedir_numero("Diámetro: ")
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


#funcion para borrar un cuerpo celeste
def borrar_cuerpo():

    while True:

        nombre = pedir_texto("\n🗑 Nombre del cuerpo a eliminar: ")

        encontrado = False

        for c in cuerpos:

            if c["nombre"].lower() == nombre.lower():

                cuerpos.remove(c)

                print(Fore.GREEN + f"\n✅ '{nombre}' fue eliminado correctamente.")

                encontrado = True

                break

        if encontrado:
            break

        else:
            print(Fore.RED + "\n❌ No se encontró ese cuerpo celeste.")
            print(Fore.YELLOW + "Intenta nuevamente.")

# FUNCIÓN PARA MODIFICAR DATOS
def modificar_cuerpo():

    print(Fore.YELLOW + "\n✏ MODIFICAR CUERPO CELESTE ✏\n")

    nombre = pedir_texto("Nombre del cuerpo a modificar: ")

    encontrado = None

    # buscar el cuerpo
    for c in cuerpos:

        if c["nombre"].lower() == nombre.lower():
            encontrado = c
            break

    # validar existencia
    if encontrado is None:

        print(Fore.RED + "\n❌ Cuerpo no encontrado.")
        return

    # mostrar datos actuales
    print(Fore.CYAN + "\n📋 DATOS ACTUALES:\n")

    print(tabulate(
        [encontrado],
        headers="keys",
        tablefmt="fancy_grid",
        showindex=False
    ))

    # pedir nuevos datos
    print(Fore.YELLOW + "\n🔧 Ingresa los nuevos datos:\n")

    encontrado["nombre"] = pedir_texto("Nuevo nombre: ")
    encontrado["tipo"] = pedir_texto("Nuevo tipo: ")
    encontrado["ubicacion"] = pedir_texto("Nueva ubicación: ")
    encontrado["distancia (ly)"] = pedir_numero("Nueva distancia: ")
    encontrado["diametro (km)"] = pedir_numero("Nuevo diámetro: ")

    print(Fore.GREEN + "\n✅ Datos modificados correctamente.")
 
# FUNCIÓN PARA BUSCAR POR INICIAL
def buscar_inicial():

    print(Fore.YELLOW + "\n🔠 BUSCAR POR INICIAL 🔠\n")

    letra = pedir_texto("Ingresa una letra: ")

    # validar
    while len(letra) != 1 or not letra.isalpha():

        print(Fore.RED + "❌ Ingresa solo UNA letra válida.")

        letra = pedir_texto("Ingresa una letra: ")

    encontrados = []

    # recorrer cuerpos
    for c in cuerpos:

        # verificar inicial
        if c["nombre"].lower().startswith(letra.lower()):

            encontrados.append(c)

    # mostrar resultados
    if encontrados:

        print(Fore.GREEN + "\n✅ CUERPOS ENCONTRADOS:\n")

        print(tabulate(
            encontrados,
            headers="keys",
            tablefmt="fancy_grid",
            showindex=False
        ))

    else:

        print(Fore.RED + "\n❌ No hay cuerpos con esa inicial.")
        
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

    # ELIMINAR CUERPO
    elif opcion == "4":

        borrar_cuerpo()

    # MODIFICAR CUERPO
    elif opcion == "5":
     
        modificar_cuerpo()

    # BUSCAR POR LETRA INICIAL
    elif opcion =="6":
    
       buscar_inicial()
    
    # GUARDAR Y SALIR
    elif opcion == "7":

        guardar()

        print(Fore.CYAN + "\n🚀 Cerrando sistema astronómico...\n")

        break

    # OPCIÓN INVÁLIDA
    else:

        print(Fore.RED + "\n❌ Opción inválida.")

    input(Fore.YELLOW + "\nPresiona ENTER para continuar...")
