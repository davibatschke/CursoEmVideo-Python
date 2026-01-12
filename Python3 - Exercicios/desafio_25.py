# DESAFIO 25 do Curso de Python:
# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome_pessoa = input('Digite o seu Nome Completo: ').strip()
print(f'Seu nome tem "Silva"? {'silva' in nome_pessoa.lower()}')