#Verificação de Ano Bissexto Crie um programa que peça um ano ao usuário e informe se ele é bissexto ou não. 
#Regras para ser bissexto:
#Divisível por 4
#Não pode ser divisível por 100, exceto se também for divisível por 400.

# Solicita ao usuário que insira um ano
ano = int(input("Digite um ano: "))

# Verifica se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")

    
    
# % → Operador de módulo (resto da divisão).
# and → Operador lógico "E", que exige que ambas as condições sejam verdadeiras.
# or → Operador lógico "OU", que exige que pelo menos uma condição seja verdadeira.
# != → Diferente de (compara se dois valores não são iguais).
# == → Igual a (compara se dois valores são iguais).
