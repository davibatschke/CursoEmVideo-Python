# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
# Considere US$ 1.00 = R$ 3.27

dinheiro_conta = float(input('Digite quanto Dinheiro voce tem: '))
valor_dolar = 3.27

print(f'Voce pode ter US$ {dinheiro_conta * valor_dolar}')