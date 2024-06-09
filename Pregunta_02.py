"""""

Problema 2:
Cree un programa el cual cumpla con las siguientes especificaciones:
- Solicite al usuario el nombre de una fuente a utilizar. En caso no sé ingrese ninguna
fuente, su programa deberá seleccionar de forma aleatoria la fuente a utilizar.
- Solicite al usuario un texto.
- Finalmente, su programa deberá imprimir el texto solicitado usando la fuente
apropiada.

"""""


#pip install pyfiglet

import pyfiglet
import random

def main():
    fonts = pyfiglet.FigletFont.getFonts()

    font_name = input("Ingrese el nombre de la fuente (o presione Enter para una fuente aleatoria): ").strip()

    if not font_name:
        font_name = random.choice(fonts)
    else:
        if font_name not in fonts:
            print("Fuente no válida. Seleccionando una fuente aleatoria.")
            font_name = random.choice(fonts)

    text = input("Ingrese el texto a imprimir: ")

    figlet = pyfiglet.Figlet(font=font_name)

    print(figlet.renderText(text))

if __name__ == "__main__":
    main()