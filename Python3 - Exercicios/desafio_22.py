# DESAFIO 22 do Curso em Python:
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome_completo = input('Digite o seu Nome Completo: ').title()

print(f'\nAnalisando o seu Nome...')
print(f'Seu nome em maiúsculas, fica: {nome_completo.upper()}')
print(f'Seu nome em minúsculas, fica: {nome_completo.lower()}')

nome_separado = nome_completo.split()

print(f'O seu primeiro nome {nome_separado[0]} tem {len(nome_separado[0])} letras.')
print(f'O seu nome completo tem {len(nome_completo)-nome_completo.count(' ')} letras no total.')