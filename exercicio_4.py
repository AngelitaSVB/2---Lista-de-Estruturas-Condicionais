#Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo o resultado.

# Solicita ao usuário que insira um número
num = float(input("Digite um número: "))

# Verifica se o número é positivo ou negativo e calcula o resultado
if num > 0:
    resultado = num * 2  # Calcula o dobro se for positivo
else:
    resultado = num * 3  # Calcula o triplo se for negativo

# Exibe o resultado
print(f"O resultado é: {resultado}")