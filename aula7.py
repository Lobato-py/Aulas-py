'''
Varáiveis são usadas para salvar algo na memória do computador.
PEP8: inicie variáveis com letras minúsculas, pode usar números e underline _.
O sinal de = é o operador de atribuição. Ele é usado para atribuir
um valor a um nome (variável).
Uso: nome_da_variavel = expressão
'''

nome_completo = 'Gustavo Lobato'
soma_dois_mais_dois = 2 + 2
print(nome_completo, soma_dois_mais_dois)
# PS: variáveis NÃO SÃO usadas para abreviar códigos, são utilizadas para tornar o código
# mais legível.

print(int('1'), type(int('1'))) # Não é prudente escrever o código ASSIM.

int_um = int('1') # caso eu precise mudar o valor, não vou precisar alterar inúmeras linhas
#de códigos.
print(int_um, type(int_um)) # MUITO mais otimizado, sem repetição desnecessária.

# SEMPRE ser descritivo nas variáveis, para bater o olho e entender logo de cara o que era.
# na linha 17, é um exemplo do que NÃO fazer como nome de varíavel.

nome = 'Gustavo'
idade = 20
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade:', idade)
print('É maior?', maior_de_idade)