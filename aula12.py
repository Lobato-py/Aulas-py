'''
Aula sobre formatação/função format
'''

a = 'AAAA'
b = 'B'
c = 1.1
# parametros nomeados = se um for nomeado, TODOS OS SEGUINTES precisam ser nomeados
formato = 'a={nome1} a={nome1} a={nome1} b={nome2} c={nome3:.2f}'.format(nome1=a,nome2=b,nome3=c)
# normalmente na programação, TUDO começa do zero, principalmente índices, ou seja
# a, b, c = 0, 1, 2

print(formato)
