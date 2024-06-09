"""""

Problema 6:
Una forma de medir la complejidad de un programa es contar su número de líneas de código
(LOC), excluyendo las líneas en blanco y los comentarios. Por ejemplo, un programa como
Del código se observa que este solo tiene dos líneas de código, no cuatro, ya que su primera
línea es un comentario y su segunda línea está en blanco (es decir, solo espacios en blanco).
Esto no es tanto, por lo que es probable que el programa no sea tan complejo.
Implemente un programa donde se le solicitará al usuario la ruta de un archivo .py (nombre y
ruta). Y retorne la cantidad de líneas de código de ese archivo, excluyendo los comentarios y
líneas en blanco. Si el usuario ingresa una ruta inválida o si el nombre del archivo no termina en
.py, su programa no retornará ningún resultado.

"""""


def contar_lineas_codigo(archivo):
    try:
        with open(archivo, 'r') as f:
            lineas_codigo = 0
            for linea in f:
                linea = linea.strip()  # Eliminar espacios en blanco al principio y al final
                if linea and not linea.startswith("#"):
                    lineas_codigo += 1
        return lineas_codigo
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except IOError:
        print("Error al leer el archivo.")


def main():
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    if ruta_archivo.endswith('.py'):
        lineas_codigo = contar_lineas_codigo(ruta_archivo)
        if lineas_codigo is not None:
            print("Cantidad de líneas de código:", lineas_codigo)
    else:
        print("La ruta no es un archivo .py válido.")


if __name__ == "__main__":
    main()
