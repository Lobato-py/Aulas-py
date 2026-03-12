# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5 6
# G u s t a v o
#-7-6-5-4-3-2-1

# nome = 'Gustavo'
# # print(nome[2])
# # print(nome[-5])
# print('s' in nome)
# print('z' in nome)
# print('tavo' in nome)
# print('z' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não está em {nome}')