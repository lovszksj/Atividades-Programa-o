# colocamos o valor de 0 para declarar a variável, já que ela irá atualizar o valor dela no laço for
a = 0
b = 0
c = 0
valorp = 0
# primeiro fazemos dois laços para que a seja menor que b e depois faça a conta para que c maior que todos
for a in range (1,1001):
    for b in range (a + 1,1001):
        c = 1000 - a - b
        # aqui verificamos o triplo pitagórico e fazemos a soma para ver se os valores batem com o valor de 1000, como pedido na questão.
        if a**2 + b**2 == c**2:
            valorp = a + b + c
            print(f"triplo pitagorico encontrado: {a}, {b}, {c}")
            print(f"Valor da soma de abc: {valorp}")
            