#Faça um programa em Python que leia a média de duas avaliações (P1 e P2). Calcule e mostre a média final do aluno. Calcule e mostre se o aluno foi APROVADO ou REPROVADO, sabendo que a média para aprovação deve ser maior ou igual a 7.

# Solicita ao usuário que insira as notas das duas avaliações
P1 = float(input("Digite a nota da P1: "))
P2 = float(input("Digite a nota da P2: "))

# Calcula a média final
media_final = (P1 + P2) / 2

# Verifica se o aluno foi aprovado ou reprovado
if media_final >= 7:
    status = "APROVADO"
else:
    status = "REPROVADO"

# Exibe a média final e o status do aluno
print(f"Média Final: {media_final:.2f}")
print(f"Status: {status}")
