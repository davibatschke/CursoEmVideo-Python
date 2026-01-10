# Crie um script Python que leia dois numeros e tente mostrar a soma entre eles

# ESTA VERSAO NAO FUNCIONA! Isso por causa dos tipos primitivos (aula_06.py)
# Ou melhor, o Python reconhece o Input() normalmente como uma string (texto)
# Para isso precisamos definir o tipo de dado que devera vir do Input()

primeiro_numero = input('Primeiro numero:' )
segundo_numero = input('Segundo numero:' )
soma = primeiro_numero + segundo_numero

print('A soma vale', soma)