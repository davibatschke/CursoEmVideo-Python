# Condicoes Aninhadas sao Estruturas dentro de outras Estruturas.
# Temos tambem a Estrutura Condicional Composta, que eh o caso abaixo!

nome = str(input('Digite o seu Nome: '))

# IF - Significa "Se" usado para verificar uma condicao 
if nome == 'Davi' or nome == 'Pedro':
    print('Que nome Interessante!')

# ELIF - Significa "Senao, se" tambem usado para verificar uma condicao
elif nome == 'Alice' or nome == 'Camila':
    print('Que nome Bonito!')

# ELSE - Significa  "Senao" que eh usado quando nenhuma das condicoes acima sao "validas"
else:
    print('Que nome legal!')

print(f'Tenha um bom dia, {nome}!')