# código feito por Jullyana Pessoa e João Victor Gomes

# como liberado na questão, importamos a função random para sempre gerar um número aleatório
import random
# utilizamos o try e except para que caso o usuário digite algo sem ser um número o programa não trave
try:
    # declaramos a variável com a importação do random.randint, que sempre irá sortear um número de 1 a 100
    numero = random.randint(1, 100)
    # já essas declaramos para utilizar na exibição dos intervalos 
    nmaximo = 100
    nminimo = 1

    # aqui iniciamos o jogo de tentativa para acertar o número
    resposta1= int(input("Digite qual número você acha que foi sorteado: "))
    # caso acerte, irá aparecer a mensagem de acerto
    if resposta1 == numero:
        print("Parabéns! Você acertou")
    else:
        if resposta1 < numero:
            nminimo = resposta1 + 1
        else:
            nmaximo = resposta1 - 1
            # caso erre, irá aparecer a estimativa/intervalo dos números no qual o usuário digitou
        print("Tente entre", nminimo, "e", nmaximo)

        # e aparecerá novamente a pergunta de "chute" de qual número foi sorteado, assim repetindo o mesmo processo explicando anteriormente
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

                # como solicitado na questão, serão apenas 4 tentativas, dessa vez caso a pessoa erre novamente
                resposta4 = int(input("Não foi dessa vez! Digite outro número: "))
                if resposta4 == numero:
                    print("Parabéns! Você acertou")
                else:
                    # irá aparecer qual era o número e falando para o usuário tentar novamente
                    print("Infelizmente não foi dessa vez! Tente novamente uma outra hora")
                    print("O número sorteado foi:", numero)
except  ValueError:
    print("Digite um valor válido")


