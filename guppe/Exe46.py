
numeros = []
pares = []
impares = []

# Leitura dos números e adição à lista principal
while True:
    numero = input("Digite um número (ou 'parar' para encerrar): ")

    if numero.lower() == 'parar':
        break

    numeros.append(int(numero))

# Separando os números pares e ímpares
for num in numeros:
    if num % 2 == 0:  # Se o número é par
        pares.append(num)
    else:
        impares.append(num)

# Exibindo as listas
print("Lista principal:", numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)

