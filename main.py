#Las librerias, df =dataframe pd pandas
import pandas as pd

df = pd.read_excel("cuerpos_celestes.xlsx")
cuerpos = df.to_dict(orient="records")
#ESTE ES EL MENU, SI TIENEN MAS IDEAS DEL MENU PODEMOS AGREGARLAS
while True:
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
        print("Opción inválida")