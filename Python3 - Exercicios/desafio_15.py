# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias_alugados = int(input('Por quantos dias o carro foi alugado? '))
km_percorridos = int(input('Por quantos KM voce andou? '))
calculo_preco = (60 * dias_alugados) + (0.15 * km_percorridos)

print(f'O total a pagar eh R$ {calculo_preco}')