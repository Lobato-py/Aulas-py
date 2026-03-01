"""
Aula sobre a função: Input
"""

# a função "input" armazena dados/informações dadas pelo usuário
# nome = input('Qual o seu nome? ') #Enquanto o usuário não retornar uma resposta, o código para aqui
# print(f'Seu nome é {nome}') # -> sempre retorna string

# numero_1 = input('Digite um número: ')
# numero_2 = input('Digite outro número: ')

# print(f'A soma dos números: {numero_1 + numero_2}') # -> como retorna str, aqui ocorre a concatenação
# # Logo: 5 + 2 = 25, e não 7

numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: ')) # convertendo eles, porém de uma maneira ruim !!!
#Se caso o usuário escreva QUALQUER letra, vai quebrar por completo todo o código, por isso é ruim

print(f'A soma dos números é = {numero_1 + numero_2}')