# operacoes_matematicas.py

# Solicita dois números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Solicita a operação desejada
operacao = input("Escolha a operação (+, -, *, /): ")

# Realiza a operação e exibe o resultado
if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: Divisão por zero não é permitida!"
else:
    resultado = "Operação inválida!"

print("Resultado:", resultado)
