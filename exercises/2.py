#Eliminar todos os símbolos e algarismos.
import re

text = input("Insira um texto: ")
text = re.sub(r'[^a-zA-Z]', '', text)

print(text)