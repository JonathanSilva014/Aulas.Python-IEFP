# Inicializando contadores
pessoas_mais_25 = 0
homens_menos_17 = 0
mulheres_registradas = 0
menores_registrados = 0

while True:
    print("[ 1 ] - Registrar pessoa")
    print("[ 2 ] - Nº Pessoas registradas")
    print("[ 3 ] - Apagar um registro")
    print("[ 4 ] - Sair")

    print("Qual a sua opção:")
    opcao = int(input("-----> "))

    if opcao == 1:
        nome = input("Digite o nome da pessoa: ")
        idade = int(input("Digite a idade da pessoa: "))
        sexo = input("Essa pessoa é Feminina ou Masculina: ")

        # Verificando condições para contadores
        if idade > 25:
            pessoas_mais_25 += 1

        if sexo.lower() == 'masculina' and idade < 17:
            homens_menos_17 += 1

        if sexo.lower() == 'feminina':
            mulheres_registradas += 1

        if idade < 18:
            menores_registrados += 1

        print(f"{nome} registrado com sucesso.")
        continuar = input("Quer continuar a registrar pessoas? (Sim/Não): ").lower()
        if continuar != "sim":
            break

    elif opcao == 2:
        print(f"Há {pessoas_mais_25} pessoas com mais de 25 anos.")
        print(f"Foram registrados {homens_menos_17} homens com menos de 17 anos.")
        print(f"Foram registradas {mulheres_registradas} mulheres.")
        print(f"Foram registrados {menores_registrados} menores de idade.")

    elif opcao == 3:
        print("Um registro foi apagado!")

    elif opcao == 4:
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

print("Obrigado e volte sempre!")
