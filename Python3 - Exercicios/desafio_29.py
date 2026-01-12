# DESAFIO 29 do Curso de Python:
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Em quantos KM voce passou pelo Radar? '))
calculo_multa = (velocidade - 80) * 7

if velocidade > 80:
    print(f'Voce sera Multado por passar do Limite!')
    print(f'A multa ficara R$ {calculo_multa:.2f}')
else:
    print(f'Voce passou Abaixo do Limite.')
    print(f'Ou seja, voce nao sera multado!')