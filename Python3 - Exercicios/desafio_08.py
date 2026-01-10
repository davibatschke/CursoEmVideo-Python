# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

metros = int(input('Digite um Valor em Metros: '))
converter_cm = metros *  100
converter_mm = metros * 1000

print(f'{metros}m em Centimetros: {converter_cm}')
print(f'{metros}m em Milimetros: {converter_mm}')