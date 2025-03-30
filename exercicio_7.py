#Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#para homens: (72.7 * h) – 58;
# para mulheres: (62.1 * h) – 44.7.

# Solicita ao usuário que insira a altura e o sexo
altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite seu sexo (M para masculino, F para feminino): ").strip().upper()

# Calcula o peso ideal com base no sexo
if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
elif sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = None
    print("Sexo inválido. Use M para masculino ou F para feminino.")

# Exibe o resultado se o sexo for válido
if peso_ideal is not None:
    print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
