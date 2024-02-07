valor1 = int(input("Introduza o primeiro valor: "))
valor2 = int(input("Introduza o segundo valor: "))
valor3 = int(input("Introduza o terceiro valor: "))

opcao = 0

while opcao != 5:
    print("\nEscolha uma opção:")
    print("1 - Somar") # essa opção vai fazer com que some todos os 3 numeros
    print("2 - Multiplicar") # essa opção vai fazer com que multiplique todos os 3 numeros
    print("3 - Maior") # essa opção vai mostrar o maior dos 3 numeros
    print("4 - Novos Números") # voce vai digitar novos numeros
    print("5 - Sair")

    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 1:
        resultado = valor1 + valor2 + valor3
        print(f"A soma dos valores é: {resultado}")
    elif opcao == 2:
        resultado = valor1 * valor2 * valor3
        print(f"O produto dos valores é: {resultado}")
    elif opcao == 3:
        maior_valor = max(valor1, valor2, valor3)
        print(f"O maior valor é: {maior_valor}")
    elif opcao == 4:
        valor1 = int(input("Introduza o novo valor 1: "))
        valor2 = int(input("Introduza o novo valor 2: "))
        valor3 = int(input("Introduza o novo valor 3: "))
    elif opcao == 5:
        print("Saindo do programa...")
    else:
        print("Opção inválida. Tente novamente.")

print("======================================OUTRO PROGRAMA=====================================")

print("Qual clube foi campeão da Champions League na temporada 2003-2004?")

print("A. Real Madrid de RONALDO")
print("B. Porto de JOSE MOURINHO")
print("C. Juventus de BUFFON")
print("D. Milan de SEEDORF")

resposta_certa = "B"

while True:
    resposta_usuario = input("Escolha a opção correta (A, B, C ou D): ").upper()

    if resposta_usuario == resposta_certa:
        print("Parabéns! Você acertou.")
        break
    else:
        print("Ops! Resposta incorreta. Tente novamente.")



