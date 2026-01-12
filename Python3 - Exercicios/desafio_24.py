# DESAFIO 24 do Curso de Python:
# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

nome_cidade = input('Digite o nome de uma Cidade: ').lower().strip()
print(f'Sua cidade tem Santo no comeco? {nome_cidade[:5] == 'santo'}')