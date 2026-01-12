# No Python podemos modificar o seu Terminal e customizar ele atraves do padrao ANSI
# \033[STYLE;TEXT;BACKm -> Este eh o jeito que usamos para customizar o Terminal

# STYLE:
# 0 - None, sem configuracao
# 1 - Bold, letras em negrito
# 4 - Underline, letras com sublinhado
# 7 - Negative, letras trocam de cor com o fundo

# TEXT:
# 30 - Troca a cor do Texto para Branco
# 31 - Troca a cor do Texto para Vermelho
# 32 - Troca a cor do Texto para Verde
# 33 - Troca a cor do Texto para Amarelo
# 34 - Troca a cor do Texto para Azul
# 35 - Troca a cor do Texto para Magenta
# 36 - Troca a cor do Texto para Ciano
# 37 - Troca a cor do Texto para Cinza

# BACK:
# 40 - Troca a cor do Fundo para Branco
# 41 - Troca a cor do Fundo para Vermelho
# 42 - Troca a cor do Fundo para Verde
# 43 - Troca a cor do Fundo para Amarelo
# 44 - Troca a cor do Fundo para Azul
# 45 - Troca a cor do Fundo para Magenta
# 46 - Troca a cor do Fundo para Ciano
# 47 - Troca a cor do Fundo para Cinza

# Para ver o resultado, basta rodar o programa
print('\033[4;35;40mOla mundo!')
print('\033[1;34;42moi terminal doidao\033[m')
print('\033[7;30;43moooomagaaawww\033[m')