# Podemos fazer Modificacoes, Fatiamento, e outros numa String
# No Python os caracteres de uma string (str) comecam a serem contados do 0.

frase1 = 'Curso em Video Python'
frase2 = '  Aprenda Python   '

print(frase1[9:13]) # Retornaria do 'V' ate o 'e' o ultimo (13) nao eh contado
print(frase1[0:21]) # Retornaria do primeiro caractere ate o ultimo, porem nao eh muito recomendado
print(frase1[9:21:2]) # Retornaria do 'V' ate o ultimo caractere, porem indo de 2 em 2
print(frase1[0::3]) # Retornaria do primeiro caractere ate o ultimo pulando de 3 em 3 caracteres

print(len(frase1)) # Len() serve para saber qual o tamanho de uma string contando os espacos
print(frase1.capitalize()) # Capitalize() deixa o primeiro caractere da string em maiusculo
print(frase1.upper()) # Upper() deixa todos os caracteres da string em maiusculo
print(frase1.lower()) # Lower() deixa todos os caracteres da string em minusculo
print(frase2.strip()) # Strip() serve para remover os espacos inuteis de uma string
print(frase1.split()) # Split() serve para separar as palavras de uma string