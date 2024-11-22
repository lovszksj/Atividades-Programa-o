# código feito por Jullyana Pessoa
import random
try:
    numero = random.randint(1, 100)
    nmaximo = 100
    nminimo = 1

    resposta1= int(input("Digite qual número você acha que foi sorteado: "))
    if resposta1 == numero:
        print("Parabéns! Você acertou")
    else:
        if resposta1 < numero:
            nminimo = resposta1 + 1
        else:
            nmaximo = resposta1 - 1
        print("Tente entre", nminimo, "e", nmaximo)

        resposta2 = int(input("Não foi dessa vez! Digite outro número: "))
        if resposta2 == numero:
            print("Parabéns! Você acertou")
        else:
            if resposta2 < numero:
                nminimo = resposta2 + 1
            else:
                nmaximo = resposta2 - 1
            print("Tente entre", nminimo, "e", nmaximo)

            resposta3 = int(input("Não foi dessa vez! Digite outro número: "))
            if resposta3 == numero:
                print("Parabéns! Você acertou")
            else:
                if resposta3 < numero:
                    nminimo = resposta3 + 1
                else:
                    nmaximo = resposta3 - 1
                print("Tente entre", nminimo, "e", nmaximo)
            
                resposta4 = int(input("Não foi dessa vez! Digite outro número: "))
                if resposta4 == numero:
                    print("Parabéns! Você acertou")
                else:
                    print("O número sorteado foi:", numero)
                    print("Infelizmente não foi dessa vez! Tente novamente uma outra hora")

except  ValueError:
    print("Digite um valor válido")


