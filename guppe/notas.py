soma = 0
contador = 0

while True:
    entrada = input("Digite um número inteiro (ou 'parar' para encerrar): ")

    # Verifica se o usuário quer encerrar o programa
    if entrada.lower() == 'parar':
        break

    # Verifica se a entrada é um número inteiro
    if entrada.isdigit():
        numero = int(entrada)
        soma += numero
        contador += 1
    else:
        print("Por favor, digite um número inteiro válido.")


print(f"Você inseriu {contador} números e a soma deles é: {soma}")

