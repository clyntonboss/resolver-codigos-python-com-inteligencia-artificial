# verificar_palindromo.py

# Solicita uma palavra ao usuário
palavra = input("Digite uma palavra: ").lower().replace(" ", "")

# Inverte a palavra
palavra_invertida = palavra[::-1]

# Verifica se é palíndromo
if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo!")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
