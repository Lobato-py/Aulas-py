'''
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
'''
# o X e o Y são parametros( váriavel ), que podem ser imbuidos de valores/argumentos.
def Soma(x, y, z):
    # Definição
    print(f'{x = }  y = {y}  {z = }', '|', 'x + y + z =', x + y + z)

# os valores 1 e 2 são os argumentos, onde estão dando valor aos parametros.
Soma(1, 2, 3)
Soma(1, y=2, z=5) # se você nomear um argumento, todos os seguintes também precisarão ser nomeados.


print(1, 2, 3, sep='-')