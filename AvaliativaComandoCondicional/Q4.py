# código feito por Jullyana Pessoa e João Victor Gomes

# utilizamos o try e except para que caso o usuário digite algo sem ser um número, o programa não trave
try:
    # pedimos para o usuário digitar o ano
    ano = int(input("Digite um ano: "))

    # com o valor guaradado na variável, fizemos o cálculo para descobrirmos se o ano é bissexto ou não
    # pois se o valor for divisel por 4, é bissexto, mas também existe a opção de que se o número for divisível por 100 e por 400, também é bissexto
    if (ano % 100 != 0 and ano % 4 == 0) or (ano % 400 == 0):
        print("Esse ano é bissexto!")
    else:
        # se ele for divisível apenas por 100 ou outro valor, ele não é considerado
        print("Esse ano não é bissexto")

except ValueError:
    print("Digite apenas número!")
    
