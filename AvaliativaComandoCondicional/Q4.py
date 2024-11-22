#codigo feito por Jullyana Pessoa
try:
    ano = int(input("Digite um ano: "))
    
    if (ano % 100 != 0 and ano % 4 == 0) or (ano % 400 == 0):
        print("Esse ano é bissexto!")
    else:
        print("Esse ano não é bissexto")

except ValueError:
    print("Digite apenas número!")
    