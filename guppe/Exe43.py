numeros = []  # Cria uma lista vazia

for cont in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)  # Adiciona o número à lista

# Itera sobre a lista e imprime os elementos
for i, v in enumerate(numeros):
    print(f"Elemento {i + 1}: {v}")
