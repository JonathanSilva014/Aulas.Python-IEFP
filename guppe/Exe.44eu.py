def main():
    numeros = []

    # Solicita ao usuário que insira números até que ele deseje parar
    entrada = input("Digite um número (ou qualquer letra para parar): ")
    while entrada.isdigit():  # Verifica se a entrada é um número
        num = float(entrada)

        # Verifica se o número já está na lista
        if num not in numeros:
            numeros.append(num)
        else:
            print("Número já está na lista. Não será adicionado novamente.")

        entrada = input("Digite um número (ou qualquer letra para parar): ")

    # Ordena a lista em ordem decrescente
    numeros.sort(reverse=True)

    # Exibe os números em ordem decrescente
    print("\nNúmeros em ordem decrescente:")
    for numero in numeros:
        print(numero)

if __name__ == "__main__":
    main()

