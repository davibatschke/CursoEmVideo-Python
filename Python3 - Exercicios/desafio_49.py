# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input('Digite um numero: '))

for tabuada in range(1, 11):
    print(f'{numero} x {tabuada:2} = {numero * tabuada}')