import random

# Criando os jogadores
jogador1 = {"Nome": input("Digite o nome do Primeiro Jogador: "), "Dado": random.randint(1, 6)}
jogador2 = {"Nome": input("Digite o nome do Segundo Jogador: "), "Dado": random.randint(1, 6)}
jogador3 = {"Nome": input("Digite o nome do Terceiro Jogador: "), "Dado": random.randint(1, 6)}
jogador4 = {"Nome": input("Digite o nome do Quarto Jogador: "), "Dado": random.randint(1, 6)}

# Criando uma lista com os jogadores
jogadores = [jogador1, jogador2, jogador3, jogador4]

# Ordenando os jogadores com base nos valores dos dados
ranking = sorted(jogadores, key=lambda x: x["Dado"], reverse=True)

# Exibindo o ranking
print("\nRanking de Jogadores:")
for i, jogador in enumerate(ranking, start=1):
    print(f"{i}. {jogador['Nome']} - Dado: {jogador['Dado']}")


import random
import time

def jogada(jogador):
    print(f"\n{jogador['Nome']} está jogando...")
    time.sleep(2)  # Pausa de 2 segundos para simular a jogada
    jogador["Dado"] = random.randint(1, 6)
    print(f"{jogador['Nome']} jogou o dado e obteve: {jogador['Dado']}")

# Criando os jogadores
jogador1 = {"Nome": input("Digite o nome do Primeiro Jogador: "), "Dado": 0}
jogador2 = {"Nome": input("Digite o nome do Segundo Jogador: "), "Dado": 0}
jogador3 = {"Nome": input("Digite o nome do Terceiro Jogador: "), "Dado": 0}
jogador4 = {"Nome": input("Digite o nome do Quarto Jogador: "), "Dado": 0}

# Criando uma lista com os jogadores
jogadores = [jogador1, jogador2, jogador3, jogador4]

# Jogadas dos jogadores
for jogador in jogadores:
    jogada(jogador)

# Ordenando os jogadores com base nos valores dos dados
ranking = sorted(jogadores, key=lambda x: x["Dado"], reverse=True)

# Exibindo o ranking
print("\nRanking de Jogadores:")
for i, jogador in enumerate(ranking, start=1):
    print(f"{i}. {jogador['Nome']} - Dado: {jogador['Dado']}")
