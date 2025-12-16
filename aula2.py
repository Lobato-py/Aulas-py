# Função print():
print(12, 34) # Tudo o que estiver dentro dos () é chamado de "argumentos".
print(56, 78) # -> NÃO USE LETRA MAIÚSCULA PARA CHAMAR FUNÇÕES!

# Argumentos nomeados:

print(56, 78, sep='-') # indiferente qual aspas usar
print(12, 34, sep="-")

# O parâmetro `sep` é um argumento nomeado que especifica 
# a string colocada entre todos os argumentos posicionais 
# passados ​​para `print`; seu valor padrão é um único 
# espaço (' '). Você pode usar aspas simples ou duplas 
# para escrever o separador (por exemplo, `sep="-"` 
# ou `sep='-'`) — ambos produzem o mesmo resultado.

# Quebras de linha:
# \r\n -> quebra de linha padrão do windows (carriage return + line feed); o Windows ja entende
# o \n sozinho, mas o \r\n é o padrão historico.
# \n -> quebra de linha padrão do linux e macOS (line feed)

print(12, 34, sep='-', end='\r\n') # Windows mais antigos.
print(56, 78, sep='-', end='\n') # sistemas baseados em unix (linux, macOS) ja entendem o \n sozinho
# Windows 11 já se aproxima desses comandos. 

print(90, 12, sep='-', end='#') # Utilizando o end de maneira com que não quebre a linha.
print(34, 56, sep='-', end='#\n') # Escreve a string '#' e depois quebra a linha com o \n.
# Também funcionaria se escrevesse o '\n##'; Ele faria a quebra de linha e depois escreveria '##'.