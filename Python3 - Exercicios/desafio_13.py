# Faca um algoritmo que le o salario de um funcionario e mostre o seu novo salario com 15% de aumento

salario_funcionario = float(input('Digite o Salario do Davi: '))
aumento = salario_funcionario + (salario_funcionario * (15/100))

print(f'O novo salario de Davi seria de R$ {aumento}')