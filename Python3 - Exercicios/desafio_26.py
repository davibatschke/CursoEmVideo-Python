# DESAFIO 26 do Curso de Python:
# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição 
# ela aparece a última vez.

frase = str(input('Digite uma Pequena Frase: ')).lower().strip()

print(f'\nEstou analisando sua Frase...')
print(f'Quantas vezes aparece a letra "A"? {frase.count('a')}')
print(f'Em que posicao ela aparece primeiro? {frase.find('a') + 1}')
print(f'Em que posicao ela aparece por ultimo? {frase.rfind('a') + 1}')