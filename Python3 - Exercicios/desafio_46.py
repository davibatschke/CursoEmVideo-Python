# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time

for contagem in range(10, -1, -1):
    print(f'Contagem: {contagem}s')
    time.sleep(1.0)

print('\nBUMM POWW')
print('estoro foi tudo')