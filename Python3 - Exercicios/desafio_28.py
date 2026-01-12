# DESAFIO 28 do Curso de Python:
# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número 
# escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

numero_aleatorio = random.randrange(0, 5)
print(f'Pensei em um Numero quero ver voce adivinhar!')

numero_escolhido = int(input('Escolha um numero de 0 a 5: '))
if numero_escolhido == numero_aleatorio:
    print(f'Parabens! Voce acertou!')
else:
    print(f'Haha! Nao foi desta vez!')