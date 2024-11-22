# código feito por Jullyana Pessoa e João Victor Gomes

# utilizamos o try e except para que caso o usuário digite algo sem ser um número, o programa não trave
try:
    #pedimos para o usuário colocar a notas
    n1 = float(input("Digite a nota da Unidade 1: "))
    n2 = float(input("Digie a nota da Unidade 2: "))

    # aqui é feita a primeira operação, para saber se o usuário foi aprovado, reprovado direntamente ou irá para a prova final 
    md = (2*n1 + 3*n2) / 5

    # aqui utilizamos o if caso o usuário tenha nota menor que 20, ele já está reprovado e sem chance de avaliação final
    if md < 20:
        print("Você está reprovado!")

    # maior ou igual a 60 o usuário está aprovado
    elif 60 <= md: 
        print ("Você está aprovado!") 

    # igual ou maior que 20 e menor que 60, o usuário irá para a última avaliação
    elif 20 <= md < 60:
        print("Você tirou", md, "e irá para a avaliação final")
        # a variável naf é declarada para a nota da avaliação final digitada pelo usuário
        naf = float(input("Digite a nota da avaliação final: "))
        # aqui o programa pega qual fórmula se adequa melhor a situação e notas do usuário
        mdf = (md + naf) / 2
        mdf1 = (2*naf + 3*n2) / 5
        mdf2 = (2*n1 + 3*naf) / 5
        # caso o resultado dessas contas for maior ou igual a 60 o usuário está aprovado
        if 60 <= mdf:
            print("Você está aprovado!")
        else: 
            # se não, reprovado
            print("Você está reprovado!")
except ValueError:
    print("Digite um valor válido")
    
