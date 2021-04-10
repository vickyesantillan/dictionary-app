import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))  # tranforma el archivo en un diccionario


def tesauro(word_1):
    word_1 = word_1.lower()
    if word_1 in data:
        return data[word_1]
    elif word_1.title() in data:
        return data[word_1.title]
    elif word_1.upper() in data:
        return data[word_1.upper()]
    elif len(get_close_matches(word_1, data.keys())) > 0:
        word_1 = get_close_matches(word_1, data.keys())[0]
        yn = input(
            "Quisiste decir %s? Escribe Y si es asi, o N si no es la palabra que querias: " % word_1)
        if yn == "Y":
            return data[word_1]
        elif yn == "N":
            return "Tu palabra es otra entonces, no existe en nuestra base de datos."
        else:
            return "No entendi que quisiste decir :("
    else:
        return "Tu palabra no existe, no existe en nuestra base de datos."


input_user = input("Palabra: ")
salida = tesauro(input_user)
if isinstance(salida, list):
    for item in salida:
        print(salida)
else:
    print(salida)
