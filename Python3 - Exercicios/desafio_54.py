# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

ano_atualizado = date.today().year
contador_maior_idade = 0
contador_menor_idade = 0

for pessoa in range(1, 8):
    ano_nascimento = int(input(f'Digite o Ano de Nascimento da {pessoa} Pessoa: '))
    calculo_idade = ano_atualizado - ano_nascimento

    if calculo_idade >= 18:
        contador_maior_idade += 1
    else:
        contador_menor_idade += 1

print('\nCom estes Anos de Nascimento, temos:')
print(f'Pessoas Maiores de Idade: {contador_maior_idade}')
print(f'Pessoas Menores de Idade: {contador_menor_idade}')