# código feito por Jullyana Pessoa e João Victor Gomes

# utilizamos o try e except para que caso o usuário digite algo sem ser um número o programa não trave
try:
    # Aqui pedimos para que o usuário digitasse os valores de seu peso e de sua altura
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite a sua altura em cm: "))

    # Como a questão pede em "m", peguamos o valor em cm, digitado pelo usuário, e dividimos por 100 para transformá-lo em m
    altura = altura / 100

    # Aqui pegamos o valor do peso e dividimos ele pela altura ao quadrado e mostramos no print qual seria o IMC
    imc = peso / altura**2
    print("O seu IMC é: ",round (imc, 1))

    # Como solicitado na questão, além de declararmos o valor do IMC também pede para falarmos do nível em qual o usuário está 
    # Começamos pelo o de menor valor e fomos aumentando até chegar ao 40 como pedido na questão, usando os comandos if de inicial e continuando com o elif
    if imc <= 18.5:
        print("Seu IMC está abaixo do normal")
    
    elif 18.6 <= imc <= 24.9: 
        print ("Seu IMC está normal")

    elif 25.0 <= imc <= 29.9: 
        print ("Seu IMC está no sobrepeso")

    elif 30.0 <= imc <= 34.9: 
        print ("Seu IMC está na obesidade grau I")

    elif 35.0 <= imc <= 39.9: 
        print ("Seu IMC está na obesidade grau II")

    elif 40.0 <= imc:
        print ("Seu IMC está na obesidade grau III")

# utilizamos os comandos try e except para o programa não travar, caso o usuário digite um valor inválido ou até mesmo letra
except ValueError: 
    print("Digite um valor válido")
