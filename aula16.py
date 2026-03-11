'''
Operadores lógicos
and (e) or (ou) not (não)
and - Todas as condições precisam ser verdadeiras.
Se qualquer valor for considerado falso, a expressão inteira será avaliada naquele valor
são considerados falsy
0 0.0 '' False
Também existe o tipo None que é usado para representar um não valor 
'''

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# # lembrando que ele da prioridade a TUDO que estiver dentro de parenteses
# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto circuito
# print(True and True and True)
# Depois que ele identifica o "False", ele não checará o restante.
# print(0 or False or 0 or 'abc') # -> sempre retorna apenas o PRIMEIRO valor True
# neste exemplo, retorna o 'abc' porque ele é True.

# senha = input('Senha: ') or 'Sem senha'
# print(senha)

# Operador lógico "not"
# usado para inverter expressões
# not True = False
# not False = True

# senha = input('Senha: ')

# if not senha:
#     print('Você não digitou nada.')

print(not True) # False
print(not False) # True
print(not 1)
print(not 0)