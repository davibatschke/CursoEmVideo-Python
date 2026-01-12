# DESAFIO 32 do Curso de Python:
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Digite um Ano qualquer: '))

if ano % 4 == 0:
    print(f'O ano {ano} eh Bissexto :D')
else:
    print(f'O ano {ano} nao eh Bissexto :c')