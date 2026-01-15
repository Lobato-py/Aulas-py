# Ordem de precedência:

# 1. (n + n) -> parênteses !PS: ELE DA PREFÊRENCIA A PARENTESES INTERNOS TAMBÉM ENTAO = (1+(1+1)) ELE RESOLVE O INTERNO PRIMEIRO
# 2. ** -> potenciação
# 3. *  / // % -> multiplicação; divisão; divisão inteira; módulo
# 4. + - -> adição; subtração

'''
Explicando a conta 1 + 1 ** 5 + 5 = 7:
    O interpretador lê sempre da esquerda para direita seu código, porém, ele tem uma ordem de
    precedência para a leitura de valores. Como descrito acima, mostra a ordem em que ele executa
    as funções para atribuição do valor da variável, logo, a conta foi feita da seguinte maneira:

    conta = 1 + 1 ** 5 + 5
    1º - pela ordem da procedência, o interpretador faz 1**5 sendo assim, um elevado na quinta
    que tem como resultado 1.
    2º - depois, ele faz o restante da conta, já que sobrou apenas as adições e subtrações:
    1 + 1(valor da potenciação) + 5 = 7.
'''

conta_1 = (1+1) ** (5+5) #1024
conta_1 = 'Qualquer coisa' # Da para mudar o valor da variável enquanto o programa roda.
# exemplo: ele calculou a conta_1 para o valor de 1024, logo após recebeu que seu novo valor era
# 'Qualquer coisa'; Logo, seu valor é 'Qualquer coisa', não mais 1024 como descrito anteriormente
print(conta_1)