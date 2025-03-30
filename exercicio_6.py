#Faça um algoritmo que leia uma variável e some 5, caso seja par ou some 8 caso seja ímpar, imprimir o resultado desta operação.

# Solicita ao usuário que insira um número inteiro
num = int(input("Digite um número inteiro: "))

# Verifica se o número é par ou ímpar e realiza a operação correspondente
if num % 2 == 0:
    resultado = num + 5  # Soma 5 se for par
else:
    resultado = num + 8  # Soma 8 se for ímpar

# Exibe o resultado
print(f"O resultado é: {resultado}")
