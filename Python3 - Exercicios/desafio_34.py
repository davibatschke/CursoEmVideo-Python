# DESAFIO 34 do Curso de Python:
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o seu Salario: '))

if salario > 1250.00:
    aumento = 1250 * (10/100)
    salario_novo = salario + aumento
if salario <= 1250.00:
    aumento = 1250 * (15/100)
    salario_novo = salario + aumento

print(f'O seu salario de R$ {salario:.2f}\nTeve um aumento de R$ {salario_novo:.2f}')