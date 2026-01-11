# AULA 08 - Utilizando Modulos em Python

# Modulos no Python sao pequenas ferramentas/bibliotecas extras que podemos usar
# Podemos usar alguns modulos como: math, os, random, secrets, e muitas outras
# Para importarmos usamos o seguinte comando: 
# import {nome da biblioteca} - Importa todas as ferramentas de uma determinada biblioteca
# from {nome da biblioteca} import {ferramenta especifica} - Importa apenas o que queremos

from math import sqrt
import random

num1 = int(input('Digite um numero: '))
print(f'A raiz de {num1} equivale a {sqrt(num1)}')

num2 = random.randint(1, 100)
print(f'Numero Aleatorio: {num2}')