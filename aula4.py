# dicas: ao pressionar ctrl + / comenta ou descomenta a linha selecionada.

"""
Tipos int e float
int - > números inteiros
O tipo int representa qualquer número positivo ou negativo.
int sem sinal é considerado positivo.

float -> Números com ponto flutuante (números reais, com parte decimal)
O tipo float representa qualquer número positivo ou negativo com ponto flutuante.
float sem sinal é considerado positivo.

A função type() mostra o tipo que o Python atribuiu ao valor.
"""

# int:
print(11) #int
print(-11) #int
print(0) #int

# float:
print(1.1, 10.11) #float
# IMPORTANTE: O separador de casas decimais é o ponto e não a vírgula!!!
print(0.0) #float
print(-1.5) #float

# Função/Classe type():
print(type('Gustavo'))
# normalmente chamada de função por conta de começar com letra minúscula, porém ela é uma classe.