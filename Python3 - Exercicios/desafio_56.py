# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho 
# e quantas mulheres têm menos de 20 anos.

soma_das_idades = 0
media_de_idade = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''
mulheres_menos_vinte_anos = 0

for pessoa in range(1, 5):
    print(f'=====[ {pessoa} PESSOA ]=====')
    nome_pessoa = str(input('Nome: '))
    idade_pessoa = int(input('Idade: '))
    genero_pessoa = str(input('Gênero (M/F): '))
    soma_das_idades += idade_pessoa

    if pessoa == 1 and genero_pessoa in 'Mm':
        idade_homem_mais_velho = idade_pessoa
        nome_homem_mais_velho = nome_pessoa
    if genero_pessoa in 'Mm' and idade_pessoa > idade_homem_mais_velho:
        idade_homem_mais_velho = idade_pessoa
        nome_homem_mais_velho = nome_pessoa
    if genero_pessoa in 'Ff' and idade_pessoa < 20:
        mulheres_menos_vinte_anos += 1
media_de_idade = soma_das_idades / 4

print(f'\nA Média de Idade do Grupo é de: {media_de_idade}')
print(f'O Homem de Maior Idade se chama: {nome_homem_mais_velho} com {idade_homem_mais_velho} anos')
print(f'E ao Total tem {mulheres_menos_vinte_anos} Mulher(es) com Menos de 20 Anos.')