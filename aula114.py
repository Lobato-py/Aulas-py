# Manipulando chaves e valores em dicionários

pessoa = {}

chave = 'nome'

pessoa[chave] = 'Gustavo' # altera o valor da 'chave'
pessoa['sobrenome'] = 'Lobato'

print(pessoa[chave])


pessoa[chave] = 'Rebeca'

del pessoa['sobrenome'] # deleta o valor de uma 'chave'
print(pessoa)
# print(pessoa['sobrenome']) # vai dar KeyError por conta que a 'chave' sobrenome foi deletada
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None: # .get tenta obter uma 'chave' dentro do dicionário
    print('não existe')

else:
    print(pessoa['sobrenome'])

# print('Isso não vai ser executado')
