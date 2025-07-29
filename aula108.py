"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1

def Escopo():
    global x # "global" manipula a variável, aqui eu digo que agora o X da função "Escopo" é o valor universal do cógido,
             # ignorando o valor da primeira váriavel X = 1.
    x = 10

    def Outra_funcao():
        x = 11
        y = 2
        print(x, y)

    Outra_funcao()
    print(x)

print(x)
Escopo()
print(x)

# pra essa aula, além dela ser uma confusão, eu não sei explicar bem ela. Vou usar o exemplo das bonecas russas para o "escopo",
# se lembre das bonecas russas, dentro de cada uma, tem uma função, e cada bonequinha pode apenas mexer na sua função



#Exemplo:

x = 1 # o primeiro valor de X está dentro do escopo mundial, não está em uma função

def Escopo():
    x = 2 # o segundo valor de X se encontra em uma função, logo dentro do "mundinho Escopo", ele vale 2
    

    def Outro_escopo():
        x = 3 # o terceiro valor de X se encontra em outra função, logo dentro do "mundinho Outro_escopo", ele vale 3
        print(x)
    
    print (x)
    Outro_escopo() # vale 3

print(x) # vale 1
Escopo() # vale 2
# ^ essa função vai falar 2 e depois 3, pois ela leu toda a função "Escopo" que tinha as seguintes ordens:
# --> X = 2 ; ler a função Outro_escopo[ X = 3 ; print(x) ] ; print(x) ; Executar a função Outro_escopo.

# o LER a função é diferente de EXECUTAR, pois pedi para que ela executasse a função que o valor de X era 3 APENAS
# depois dela EXECUTAR a função X = 2.