'''
Aula sobre:

if / elif      / else
se / se não se / se não
'''

'''
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar': # o IF consegue "viver" sozinho, não depende do ELIF ou do ELSE
    print('Você entrou no sistema')

elif entrada == 'sair': # pode se repetir VÁRIAS vezes, depende do IF
    print('Você saiu do sistema')

else: # ELSE deve ser sempre a ÚLTIMA opção, e depende sempre do IF, não funcionando caso o mesmo não exista
    print('Comando não reconhecido, digite uma opção válida.')

print('FORA DOS BLOCOS') # se caso UMA das condições seja batida dentro dos comandos, nenhum bloco irá
# se executado.
# Exemplo: Se caso o usuário digite sair, ativando o bloco ELIF, nem o IF nem o ELSE serão executados.
'''

# condicao = False
condicao1 = False
condicao2 = False
condicao3 = True # a partir que ele checar uma variável e ela for VERDADEIRA(True), ele ira ignorar o
# restante e executará apenas ela.
condicao4 = False

# if condicao: # aqui ele só será executado se caso a variável "condicao" seja True(verdadeira)
#     print('Este é o código do if')
# else:
#     print('Este o else do primeiro if')

# if 10 == 10:
#     print('Outro if')
# print('fora do if')

if condicao1:
    print('Código para condição 1')

elif condicao2:
    print('Código para condição 2')

elif condicao3:
    print('Código para condição 3')

elif condicao4:
    print('Código para condição 4')

else:
    print('Nenhuma condição foi satisfeita')

if 10 == 10:
    print('Outro if')
print('fora do if')