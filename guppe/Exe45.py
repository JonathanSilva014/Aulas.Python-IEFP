"""
numeros = []

for _ in range(5):
    numero = int(input("Digite um número: "))

    # Adiciona o número à lista na posição correta
    if not numeros or numero > numeros[-1]:
        numeros.append(numero)
        print("Numero adicionado no inicio")
    else:
        for i, v in enumerate(numeros):
            if numero <= v:
                numeros.insert(i, numero)
                break

# Imprime a lista com os números na posição correta
print("Números na posição correta:")
print(numeros)
"""
lista = list()

for c in range(0, 5):
    novo_num = int(input(f"Digite o {c+1}º numero: "))
    if c == 0:
        lista.append(novo_num)
        print(f"O numero {novo_num} foi adicionado na primeira posição. ")
    elif novo_num > lista[-1]:
        lista

