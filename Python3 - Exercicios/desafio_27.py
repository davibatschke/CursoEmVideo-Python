# DESAFIO 27 do Curso de Python:
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome_pessoa = input('Digite o seu Nome Completo: ').strip()
separando_nome = nome_pessoa.split()

print(f'O seu primeiro nome: {separando_nome[0].capitalize()}')
print(f'O seu ultimo nome: {separando_nome[-1].capitalize()}')