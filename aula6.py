# Conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# Tipos imutáveis e primitivos:
# str, int, float, bool.

print(1+1)
print('a' + 'b') # -> Isso pode ser chamado de "Polimorfismo"
# Polimorfismo é a capacidade de um operador ou função se comportar de 
# maneira diferente dependendo do tipo dos dados com os quais está operando.
# print('1' + 1) # -> TypeError
print(int('1'), type(int('1')))
print(int('1') + 1)
print(float('1')+ 1)
print(bool('')) # -> False (String vazio é False)
print(bool(' ')) # -> True (String com espaço é True)
print(str(11) + 'b')