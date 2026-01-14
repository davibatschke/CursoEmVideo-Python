# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase_completa = str(input('Digite uma Frase: ').upper().strip())
palavras_da_frase = frase_completa.split()
nova_frase_junta = ''.join(palavras_da_frase)
frase_invertida = ''

for letra in range(len(nova_frase_junta) -1, -1, -1):
    frase_invertida += nova_frase_junta[letra]

if nova_frase_junta == frase_invertida:
    print(f'Invertendo sua Frase fica: {frase_invertida}')
    print(f'E ela é um \033[0;36mPalíndromo!\033[m')
else:
    print(f'Invertendo sua Frase fica: {frase_invertida}')
    print(f'E ela \033[0;31mnao é um Palíndromo!\033[m')