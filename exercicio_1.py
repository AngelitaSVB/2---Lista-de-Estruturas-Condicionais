# Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.

# Solicita ao usuário que insira os valores de A, B e C
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

# Calcula a soma de A e B
soma = A + B

# Verifica se a soma de A e B é menor que C
eh_menor = soma < C

# Exibe o resultado na tela
if eh_menor:
    print("A soma de A + B é menor que C.")
else:
    print("A soma de A + B NÃO é menor que C.")
