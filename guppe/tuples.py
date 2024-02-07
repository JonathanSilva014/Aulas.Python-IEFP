"""
numeros_extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze",
                   "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

numero = int(input("Digite um número de 0 a 20: "))

# Verificando se o número está dentro da faixa permitida
if 0 <= numero <= 20:
    num_extenso = numeros_extenso[numero]
    print(f"O número {numero} por extenso é: {num_extenso}")
else:
    print("Número fora da faixa permitida.")
"""


"""
campeonato_espanhol = ("Barcelona","Real Madrid","Valencia","Girona","Las Palmas","Atl Madrid","Osasuna","Espanhol",
                       "Atl Bilbal","Sevillha","Real Sociedad","Real Betis","Rayo Vallecano","Osasuna","Cadiz","Granada",
                       "Alaves","Celta de Vigo","Mallorca","VillaReal","Granada","Alméria","Getafe")
# a) Os primeiros 5 classificados
primeiros_5 = campeonato_espanhol[:5]

# b) Os últimos 4 classificados
ultimos_4 = campeonato_espanhol[-4:]

campeonato_espanhol_ordenado = sorted(campeonato_espanhol)

posicao_las_palmas = campeonato_espanhol.index("Las Palmas")

print("a) Os primeiros 5 classificados:")
for posicao, time in enumerate(primeiros_5, start=1):
    print(f"{posicao}. {time}")

print("\nb) Os últimos 4 classificados:")
for posicao, time in enumerate(ultimos_4, start=len(campeonato_espanhol) - 3):
    print(f"{posicao}. {time}")

# Exibe a lista ordenada
print("\nCampeonato Espanhol em ordem alfabética:")
for time in campeonato_espanhol_ordenado:
     print(time)

print("\nLugar do Las Palmas: ", posicao_las_palmas + 1)



primeiro_numero = int(input("Digite o Primeiro Numero: "))
segundo_numero = int(input("Digite o Segundo Numero: "))
terceiro_numero = int(input("Digite o Terceiro Numero: "))
quarto_numero = int(input("Digite o Quarto Numero: "))
quinto_numero = int(input("Digite o Quinto Numero: "))

numeros = (primeiro_numero, segundo_numero, terceiro_numero, quarto_numero, quinto_numero)
"""
"""
lista = [2,3,4,5]

for i , v in enumerate (lista):
    print(i,v)
"""

"""
lista = list()

for cont in range(0, 5):
    num = int(input("Digite um numero : " ))
    lista.append(num)
    print(f"O numero {num} foi adicionado com sucesso")

for valor in lista:
    print(valor, end= "")

"""


"""
numeros = []

for cont in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)  # Adiciona o número à lista

# Encontrando o maior e o menor elemento
maior_elemento = max(numeros)
menor_elemento = min(numeros)

# Itera sobre a lista e imprime os elementos
for i, v in enumerate(numeros):
    print(f"Elemento {i + 1}: {v}")

# Imprime o maior e o menor elemento
print(f"O maior elemento é: {maior_elemento}")
print(f"O menor elemento é: {menor_elemento}")
"""

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
