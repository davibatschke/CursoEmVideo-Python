# DESAFIO 31 do Curso de Python:
# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 
# para viagens mais longas.

distancia_viagem = int(input('Quantos KM tem a sua Viagem? '))

if distancia_viagem <= 200:
    print(f'Sua viagem ficara por R$ {distancia_viagem * 0.50:.2f}')
else:
    print(f'Sua viagem ficara por R$ {distancia_viagem * 0.45:.2f}')