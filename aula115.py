'''
Métodos úteis dos dicionários em Python:

len - quantas chaves # NÃO é um método dentro do dicionário, com ressalvas
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
'''

# d1 = {
#     'nome': 'Gustavo',
#     'sobrenome': 'Lobato',
#     'idade': 20,
# }

# pessoa.setdefault('idade', 18)
# print(pessoa['idade'])
# print(len(pessoa)) # Caso você faça 'chaves' iguais, elas serão apenas contadas como UMA 'chave', mas o valor
# utilizado será sempre o último, como se fosse uma "atualização".
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# for valor in pessoa.values():
#     print(valor)
# import copy


# d1 = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0, 1, 2],
# }

# d2 = d1.copy() # Copia tudo que for imutável, nao entra em subníveis
# d2 = copy.copy seria a mesma coisa que .copy()

# # d2 = d1 # por serem valores mútaveis, a lista tanto quanto o dicionário, o sinal de '=' atribui que eles
# # se direcionam para o mesmo dicionário

# d2['c1'] = 1000 # logo se você mudar o valor de d2, vai estudar mudando o valor de d1
# d2['l1'][1] = 99999
# print(d1)
# print(d2)

# d2 = copy.deepcopy(d1) # Copia tudo que é imutável e mutável

# d2['c1'] = 1000 # logo se você mudar o valor de d2, vai estudar mudando o valor de d1
# d2['l1'][1] = 99999
# print(d1)
# print(d2)

p1 = {
    'nome': 'Gustavo',
    'sobrenome': 'Lobato',
}
# print(p1.get('nome', 'Não existe')) # Se caso não tenha a chave, ele retorna None, em vez de um KeyError

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# p1.update({
#     'nome': 'Novo valor',
#     'idade': 20,
# })

# p1.update(nome = 'novo valor', idade=20)

# tupla = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)