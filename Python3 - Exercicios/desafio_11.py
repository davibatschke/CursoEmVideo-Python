# Faca um programa que leia a altura e largura de uma parede em metros, calcule a sua area e a quantidade de tinta para pinta-la
# Sabendo que cada litro de tinta pinta uma area de 2m quadrados

altura_parede = float(input('Quanto de Altura tem a sua Parede (METROS): '))
largura_parede = float(input('Quanto de Largura tem a sua Parede (METROS): '))

calculo_area = largura_parede * altura_parede
calculo_tinta = calculo_area / 2

print('')
print(f'Uma parede de {altura_parede} de Altura e {largura_parede} de Largura')
print(f'Precisaria cerca de {calculo_tinta} Litros de Tinta!')