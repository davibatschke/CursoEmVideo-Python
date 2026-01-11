# DESAFIO 17 do Curso de Python:
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

cat_oposto = int(input('Digite um valor para o Cateto Oposto: '))
cat_adjacente = int(input('Digite um valor para o Cateto Adjacente: '))
calculo_hipotenusa = math.hypot(cat_oposto, cat_adjacente)
# math.hypot() serve para calcular o valor da hipotenusa

print(f'A Hipotenusa vale: {calculo_hipotenusa:.2f}')