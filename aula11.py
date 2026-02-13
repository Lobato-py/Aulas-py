'''
Aula sobre f-strings, utilizando o mesmo código do exercício 2 realizado anteriorimente por conta
do uso das mesmas

e um pouco de formatação de strings
'''
nome = input("Digite seu nome: ")
altura = input("Digite sua altura(exemplo: 1.86): ")
peso = input("Digite seu peso em KG: ")

altura_float= float(altura)
peso_float= float(peso)

imc= peso_float/(altura_float*altura_float)

# adicionar o f dentro das strings me permite poder usar as variáveis dentro do texto utilizando {}
print(f'{nome} tem {altura_float} de altura, pesa {peso_float} e seu IMC é: {imc:.2f}')
# no final do código no {imc:.2f} faz com que apareça apenas 2 casas decimais após o ponto

'''
A opção de código sem as fstrings seria mais ou menos assim:
print(nome, 'tem', altura, 'de altura', 'pesa', peso, 'quilos seu IMC é':, imc)
veja que o código ficaria muito mais "quebrado"
'''