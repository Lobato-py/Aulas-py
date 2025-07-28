'''
Introdução às funções (def) em Python
Funções são trechos de código usadas para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (Nada).
'''


# def Print(a, b, c): # SEMPRE usar funções começando por letra maiúscula, por favor.
#     print('várias1')
#     print('várias2')
#     print('várias3')
#     print('várias4')

# def Imprimir(a, b, c):
#     print(a, b, c)

# Imprimir(1, 2, 3)
# Imprimir(4,5,6)

def Saudacao(nome='Sem nome'): #então, atribuindo um valor a ela, mesmo que não a "chame", ela ira responder o valor atribuido antes
    print(f'Olá, {nome}!')

Saudacao('Gustavo Lobato')
Saudacao('Rebeca')
Saudacao() # nenhuma função funcionará sem um valor, ela precisa "chamar" algo