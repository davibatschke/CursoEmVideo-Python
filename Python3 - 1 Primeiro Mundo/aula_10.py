# Com o Python podemos montar programas que usam uma estrutura chamada de "Estrutura Condicional"
# Ou seja, um programa que pode seguir mais de caminho ou condicao

# EXEMPLO em Portugol:
# se idade < 18:
#   imprimir('Voce tem menos de 18')
# senao:
#   imprimir('Voce tem mais de 18')

# EXEMPLO em Python:
# if idade < 18:
#   print('Voce tem menos de 18')
# else:
#   print('Voce tem mais de 18')

nota1 = float(input('Digite a Primeira Nota: '))
nota2 = float(input('Digite a Segunda Nota: '))
nota3 = float(input('Digite a Terceira Nota: '))
calculo_media = (nota1 + nota2 + nota3) / 3

if calculo_media <= 5:
    print(f'O aluno ficou com {calculo_media:.1f}! Esta Reprovado!')
else:
    print(f'O aluno ficou com {calculo_media:.1f}! Esta Aprovado!')