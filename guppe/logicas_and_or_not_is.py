print("Bem-Vindo ao Quiz do futebol")

print("Qual clube foi campeão da Champions League de 2008 ?")
print("A Chelsea")
print("B Barcelona")
print("C Milan")
print("D Manchester United")

resposta_correta_1 = 'd'
resposta_usuario_1 = input().lower()

if resposta_usuario_1 == resposta_correta_1:
    print("Resposta Certa")
    print("Em 2008 o Manchester United foi campeão com elenco de CR7, SR Alex Fergsson e Cartilos Tevez ganhando do Chelsea nos Penaltis.")
    print(" + 3 pontos por resposta correta!")

    print("Vamos para a próxima pergunta!")
    print("Quem foi o Artilheiro da Copa America de 2010 ?")
    print("A Caça Rato")
    print("B Di Maria")
    print("C Carlinhos Bala")
    print("D Nenhuma das Alternativas")

    resposta_correta_3 = 'd'
    resposta_usuario_3 = input().lower()

if resposta_usuario_3 == resposta_correta_3:
    print(" + 3 pontos por resposta correta!")
else:
    continuar_jogando = input("Infelizmente você errou. Deseja continuar jogando? (S/N) ").lower()

    if continuar_jogando == 's':
        print("Vamos para a próxima pergunta!")
        print("Qual foi o clube campeão da taça libertadores de 2010 ?")
        print("A Internacional")
        print("B River Plate")
        print("C Once caldas")
        print("D Corinthians")

        resposta_correta_2 = 'a'
        resposta_usuario_2 = input().lower()

        if resposta_usuario_2 == resposta_correta_2:
            print("Resposta Certa")
            print("Em 2010 o internacional foi campeão da taça libertadores ganhando com Chivas de Guadalara em jogo de Ida e Volta.")
            print(" + 3 pontos por resposta correta!")
        else:
            continuar_jogando = input("Infelizmente você errou. Deseja continuar jogando? (S/N) ").lower()

            if continuar_jogando == 's':
                print("Vamos para a próxima pergunta!")
                print("Quem foi o Artilheiro da Copa America de 2010 ?")
                print("A Caça Rato")
                print("B Di Maria")
                print("C Carlinhos Bala")
                print("D Nenhuma das Alternativas")

                resposta_correta_3 = 'd'
                resposta_usuario_3 = input().lower()

                if resposta_usuario_3 == resposta_correta_2:
                    print("Resposta Certa")
                    print("Em 2010 foi ano de Copa do Mundo, e não teve Copa America, portanto Nenhuma das Alternativas.")
                    print(" Parabéns + 3 Pontos!")

    else:
        print("Obrigado por jogar!")









