#Gerar um dicionário contendo as frequencias de todas as letras no texto. 

text = input("Insira um texto: ")

frequencias = {}
    
for letra in text:
    if letra.isalpha():  # Verifica se é uma letra do alfabeto
        letra = letra.lower()  # Converte para minúscula para evitar diferenciação entre maiúsculas e minúsculas
        if letra in frequencias:
            frequencias[letra] += 1
        else:
            frequencias[letra] = 1

print(frequencias)