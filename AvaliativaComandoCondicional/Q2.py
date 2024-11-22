# código feito por Jullyana Pessoa
try:
    n1 = float(input("Digite a nota da Unidade 1: "))
    n2 = float(input("Digie a nota da Unidade 2: "))

    md = (2*n1 + 3*n2) / 5

    if md < 20:
        print("Você está reprovado!")

    elif 60 <= md: 
        print ("Você está aprovado!") 
            
    elif 20 <= md < 60:
        print("Você tirou", md, "e irá para a avaliação final")
        naf = float(input("Digite a nota da avaliação final: "))
        mdf = (md + naf) / 2
        mdf1 = (2*naf + 3*n2) / 5
        mdf2 = (2*n1 + 3*naf) / 5
        if 60 <= mdf:
            print("Você está aprovado!")
        else: 
            print("Você está reprovado!")
except ValueError:
    print("Digite um valor válido")
    