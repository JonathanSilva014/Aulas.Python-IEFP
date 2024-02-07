numeros = []

while True:
    entrada = input("Digite um número (ou 'parar' para encerrar): ")

    # Verifica se o usuário quer encerrar o programa
    if entrada.lower() == 'parar':
        break

    # Verifica se a entrada é um número
    if entrada.isdigit():
        numero = int(entrada)

        # Verifica se o número já está na lista
        if numero not in numeros:
            numeros.append(numero)
        else:
            print("Esse número já está na lista. Tente novamente.")
    else:
        print("Por favor, digite um número inteiro válido.")

# Ordena a lista em ordem decrescente
numeros.sort(reverse=True)

# Imprime os números em ordem decrescente
print("Números em ordem decrescente:")
for num in numeros:
    print(num)