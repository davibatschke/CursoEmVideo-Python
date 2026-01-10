# Desenvolva um programa que leia as duas notas de um aluno, calcule, e mostre a sua media final

nota_um = float(input('Digite a Primeira Nota: '))
nota_dois = float(input('Digite a Segunda Nota: '))

calculo = (nota_um + nota_dois) / 2
print(f'A nota final de Davi: {calculo:.1f}')