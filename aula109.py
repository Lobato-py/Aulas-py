'''
Retorno de valores das funções (return)
'''

# IMPORTANTE: print é uma função que MOSTRA na tela um valor, não que tenha valor

def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y
    # só as funções tem "return", ela retorna o valor da função

# variavel = soma(1, 2)
# variavel = int('1')
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 55))