# código feito por Jullyana Pessoa
try:
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))

    diaj = 0
    valido = True

    if (ano % 100 != 0 and ano % 4 == 0) or (ano % 400 == 0):
        bissexto = 1
    else:  
        bissexto = 0
    
    if mes < 1 or mes > 12:
        print("Mês inválido")
        valido = False

    if valido:
        if mes == 2:
            dia < 1 or dia > 28 + bissexto
            print("Dia inválido para Fevereiro!")
            valido = False

        elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12: 
            dia < 1 or dia > 31 
            if dia == 30:   
                valido = False
        else:
            if dia < 1 or dia > 30: 
                valido = False
    if valido:  
        if mes > 1:
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
                                          
        diaj = diaj + dia

        print("O dia juliano é:", diaj)
    else:
        print("Digite uma data válida!")
except ValueError:
    print ("Digite apenas números!")