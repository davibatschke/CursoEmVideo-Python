# DESAFIO 20 do Curso de Python:
# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

aluno1 = input('Nome do Primeiro Aluno: ')
aluno2 = input('Nome do Segundo Aluno: ')
aluno3 = input('Nome do Terceiro Aluno: ')
aluno4 = input('Nome do Quarto Aluno: ')
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista_alunos)
# random.shuffle() serve para alterar a ordem de elementos numa lista

print(f'Ordem de apresentação de trabalhos: \n{lista_alunos}')