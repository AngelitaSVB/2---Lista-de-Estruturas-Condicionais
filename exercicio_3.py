#Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá se somar os dois, caso contrário multiplique A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.

# Solicita ao usuário que insira dois valores inteiros
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

# Verifica se os valores são iguais
if A == B:
    C = A + B  # Soma se forem iguais
else:
    C = A * B  # Multiplica se forem diferentes

# Exibe o resultado
print(f"O resultado é: {C}")
