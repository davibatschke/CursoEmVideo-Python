# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a Razão para a PA: '))
decimo_termo = primeiro_termo + (10 - 1) * razao

for pa in range(primeiro_termo, decimo_termo + razao, razao):
    print(pa, end=' --> ')
print('Acabou!')