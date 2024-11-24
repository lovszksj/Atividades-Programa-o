# código feito por Jullyana Pessoa e João Victor Gomes

# utilizamos o try e except para que caso o usuário digite algo sem ser um número o programa não trave
try:
    # pedimos para que o usuário digite o dia, mês e ano
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))

    # declaramos aa variável que vão auxiliar nos próximos cálculos
    diaj = 0
    # criamos a variável para podermos utilizar true e false para o programa parar caso uma data inválida seja colocada, como por exemplo 31/11
    valido = True

    # utilizamos do mesmo cálculo da questão anterior para sabermos se o ano é bissexto ou não
    if (ano % 100 != 0 and ano % 4 == 0) or (ano % 400 == 0):
        # e colocamos as condições que caso seja bissexto a variável "bissexto" seja 1
        bissexto = 1
    else:  
        # se não, seja 0
        bissexto = 0

    # já aqui fizemos com o que o valor digitado em 'mes' não possa ser abaixo de 1 e nem acima de 12
    if mes < 1 or mes > 12:
        # caso o usuário digite irá aparecer o print
        print("Mês inválido")
        valido = False
    # conta feita para o mês de feveiro ter no mínimo 1 ou 28 e 29 dias (caso o ano seja bissexto)
    if valido:
        if mes == 2:
            dia < 1 or dia > 28 + bissexto
            print("Dia inválido para Fevereiro!")
            valido = False
        # igual a conta anterior, só que para esses meses terem até 31 dias
        elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12: 
            dia < 1 or dia > 31 
            valido = false
            if dia == 30: 
                valido
        else:
            # se não forem aqueles, terão até 30 dias
            if dia < 1 or dia > 30: 
                valido = False

    # fizemos a soma manualmente, sempre guardando o valor do mês anterior
    if valido:  
        if mes > 1:
            # e atualizando a variável
            diaj = diaj + 31
        if mes > 2:
            diaj = diaj + 28 + bissexto
        if mes > 3:
            diaj = diaj + 31
        if mes > 4:
            diaj = diaj + 30
        if mes > 5:
            diaj = diaj + 31
        if mes > 6:
            diaj = diaj + 30
        if mes > 7:
            diaj = diaj + 31
        if mes > 8:
            diaj = diaj + 31
        if mes > 9:
            diaj = diaj + 30
        if mes > 10:
            diaj = diaj + 31
        if mes > 11:
            diaj = diaj + 30
        if mes > 12:
            diaj = diaj + 31
        # o cálculo final para o dia juliano               
        diaj = diaj + dia

        # a mostra do resultado
        print("O dia juliano é:", diaj)
    else:
        # e caso dê algum resultado inválido durante a operação
        print("Digite uma data válida!")
        
except ValueError:
    print ("Digite apenas números!")
