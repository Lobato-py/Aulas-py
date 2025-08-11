"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Bom noite')

# print(falar_bom_dia('Gustavo'))
# print(falar_boa_noite('Gustavo'))

for nome in ['Gustavo', 'João', 'Tiago', 'Emília']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))