"""""

Problema 5:
Escriba un programa que realice las siguientes tareas (Puede usar clases y/o funciones,
también puede usar un menú para organizar su programa):
- Solicite un número entero entre 1 y 10 y guarde en un fichero con el nombre
tabla-n.txt la tabla de multiplicar de ese número, donde n es el número introducido.
- Solicite un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de
multiplicar de ese número, donde “n” es el número introducido, y la muestre por
pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de
ello.
- Solicite dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de
multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero
no existe debe mostrar un mensaje por pantalla informando de ello.

"""""

import os

def crear_tabla(n):
    filename = f"tabla-{n}.txt"
    with open(filename, "w") as file:
        for i in range(1, 11):
            file.write(f"{n} x {i} = {n*i}\n")
    print(f"Tabla de multiplicar del {n} guardada en {filename}.")

def leer_tabla(n):
    filename = f"tabla-{n}.txt"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            print(file.read())
    else:
        print(f"El archivo {filename} no existe.")

def leer_linea_tabla(n, m):
    filename = f"tabla-{n}.txt"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            if 1 <= m <= 10:
                print(lines[m-1].strip())
            else:
                print("El número de línea debe estar entre 1 y 10.")
    else:
        print(f"El archivo {filename} no existe.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Crear tabla de multiplicar")
        print("2. Leer tabla de multiplicar")
        print("3. Leer línea de la tabla de multiplicar")
        print("4. Salir")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            n = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                crear_tabla(n)
            else:
                print("El número debe estar entre 1 y 10.")
        elif choice == "2":
            n = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                leer_tabla(n)
            else:
                print("El número debe estar entre 1 y 10.")
        elif choice == "3":
            n = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                m = int(input("Ingrese la línea que desea leer (entre 1 y 10): "))
                if 1 <= m <= 10:
                    leer_linea_tabla(n, m)
                else:
                    print("El número de línea debe estar entre 1 y 10.")
            else:
                print("El número debe estar entre 1 y 10.")
        elif choice == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    menu()



