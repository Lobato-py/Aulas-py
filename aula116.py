# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Gustavo') # Dentro de parenteses ele não garante ordem.
# s1 = set() # vazio
# s1 = {'Gustavo', 1, 2, 3} # com dados


# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# s1 = {}
# l1 = [1, 2, 3, 3, 3, 3, 3, 3,]
# s1 = set(l1)
# l2 = list(s1)
# s1 = { 1, 2, 3}
# print(3 not in s1)
# for numero in s1:
#     print(numero)

# Métodos úteis:
# add, update, clear, discard
# s1 = set()
# s1.add('Gustavo')
# # s1.add(1, 2) # NÃO ACEITA mais de um valor por .add!!!
# s1.add(1)
# s1.update(('Olá mundo', 1, 2, 3, 4)) # ACEITA mais de um valor, mas só iteráveis
# # s1.clear()
# s1.discard('Olá mundo')
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# s3 = s1 | s2
# s3 = s1 & s2
# s3 = s2 - s1
# s3 = s2 ^ s1
# print(s3)

# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower)

    if 'l' in letras:
        print('Parabéns')
        break

    print(letras)