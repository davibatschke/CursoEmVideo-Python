# Faca um algoritmo que leia o preco de um produto e mostre o seu novo preco com 5% de desconto

preco_produto = float(input('Digite o Valor do Produto: '))
desconto = preco_produto - (preco_produto * (5/100)) 

print(f'O Valor do Produto com 5% de Desconto: {desconto}')