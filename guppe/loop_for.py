"""
loop for
C our Java

for(int i = 0; i < 10; i++){
}

python

for item in interavel:
    //execução do loop
    nome = "Jonathan Silva"
lista = [1, 3, 5, 7, 9]
numeros = range (1, 10)
# Exemplo de for 1

for letra in nome:
    print(letra)

#Exemplo de for 2 (iterando sobre uma lista)

for numero in lista:
    print(numero)
"""



#Exemplo de for 3 (iterando sobre um range)

"""
Range(valor_inicial, valor_final)
OBS: O Valor final não é inclusive.
for numero in range(1, 10):
    print(numero)
    
qtd = int(input("Quantas vezes esse loop vai rodar ?"))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f"Informe o {n}/{qtd} valor:"))
    soma = soma + num
print(f"a Soma é {soma}")
"""




#exercicio tal
"""
nome = "Jonathan Silva"
for i, letra in enumerate(nome):
    print(f"{i}: {letra}")
"""
"""
num = 7
for c in range(0, 10):
    print(num, " x ", c + 1, " = ", num * (c + 1))
"""



#Exercicio tal
"""
tentativas = 0
mensagem = "Bem-vindo!"
password = 1234  # Substitua pelo valor correto da senha

for c in range(0, 3):
    entrada = int(input("Insira a senha: "))
    if entrada == password:
        print(mensagem)
        break
    else:
        tentativas = tentativas + 1
        print("Tente novamente...\n")
if tentativas == 3:
    print("Usuário bloqueado")
"""



#Exercicio mais tal
"""
import time

for fogo in range(10, 0, -1):
    print(fogo)
    time.sleep(1)
    print("Feliz Ano novo!!")

"""



"""
import time

for par in range(0, 100, 2):
    if par > 1:
        print(par)
"""

"""
import time
import math

nume = int(input('Quer a tabuada de qual numero.  '))

print(int)
num = nume
for c in range(0, 10):
    print(nume, " x ", c + 1, " = ", nume * (c + 1))
"""


"""
num = int(input("Digite um numero inteiro para verificar "))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1

if tot == 2:
    print(f"O numero {num} é PRIMO, foi divisível {tot} vezes.")
else:
    print(f"O numero {num} NÃO É PRIMO, foi divisível {tot} vezes.")
"""

"""
frase = input("Digite uma frase: ")

# Remover espaços da frase
frase_sem_espacos = frase.replace(" ", "")

# Inverter a frase
frase_invertida = frase_sem_espacos[::-1]

# Verificar se é um palíndromo
if frase_sem_espacos.lower() == frase_invertida.lower():
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")
"""
"""
frase = input("Digite uma frase: ").strip().upper()
frase_sem_espacos = "".join(frase.split())  # Remover espaços da frase
frase_invertida = frase_sem_espacos[::-1]

if frase_sem_espacos.lower() == frase_invertida.lower():
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo.")

"""

"""
frase = input("Digite uma frase: ").strip().upper()
palavra = frase.split()
juntas = "".join(palavra)
inverso = juntas[::-1]

if juntas == inverso:
    print("A Palavra é um palindromo. ")
else:
    print("a palavra não é um palindromo")

print("")
print(juntas)
print(inverso)

tam = len(juntas)

for c in range(0, tam):
    if juntas[c] != inverso[c]:
        print("Não é um palindromo")
        break
    if c == tam - 1:
        print("é palindromo")
        
"""


"""
from datetime import datetime

ano_atual = datetime.now().year

idades_menores = []
idades_maiores = []

for c in range(1, 8):
    ano_nascimento = int(input(f"Digite o ano de nascimento da pessoa {c}: "))
    idade = ano_atual - ano_nascimento

    if idade >= 18:
        idades_maiores.append(idades_maiores)
    else:
        idades_menores.append(idades_menores)

"""


"""
from datetime import datetime

ano_atual = datetime.today().year

tot_maior = 0
tot_menor = 0

for pessoa in range(1, 8):
    nascimento = int(input(f"Digite o ano de nascimento da pessoa {pessoa}: "))
    idade = ano_atual - nascimento
    if idade >= 18:
        tot_maior += 1
    else:
        tot_menor += 1

print(f" todas as pessoas {tot_maior} pessoas maiores de idade")
print(f" Todas as pessoas {tot_menor} pessoas menores de idade")


"""


"""
if __name__ == '__main__':
    n = int(input("Digite um número inteiro: "))

    for i in range(n):
        print(i ** 2)
"""

"""

from datetime import datetime

ano_atual = datetime.today().year

tot_maior = 0
tot_menor = 0
maior_idade = 0
menor_idade = float('inf')
indice_maior_idade = 0
indice_menor_idade = 0


for pessoa in range(1, 11):
    nascimento = int(input(f"Digite o ano de nascimento da pessoa {pessoa}: "))
    idade = ano_atual - nascimento

    if idade >= 18:
        tot_maior += 1
        if idade > maior_idade:
            maior_idade = idade
            indice_maior_idade = pessoa
    else:
        tot_menor += 1
        if idade < menor_idade:
            menor_idade = idade
            indice_menor_idade = pessoa

print(f" a pessoa com a maior idade é {indice_maior_idade} posso considerar essa pessoa mais velha")
print(f" a pessoa com a menor iadde é {indice_menor_idade} posso consideram essa pessoa mais nova")

"""

"""
maior = 0
menor = 0

for pessoa in range(1, 11):
    idade = int(input(f"{pessoa + 1}' - digite a sua idade: "))
    if pessoa == 0
        maior = idade
        menor = idade
    else:
        if idade > maior:
            maior = idade
        elif idade < menor:
            menor = idade
print(f"A maior idade encontrada foi: {maior} anos")
print(f"A menor idade encontrada foi: {menor} anos")

"""

# exemplo do while

"""
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

opcao = 0

while opcao !=
    print("[ 1 ] - Entrar")
    print("[ 2 ] - Registrar")
    print("[ 3 ] - Apagar")
    print("[ 4 ] - Sair")

    print("Qual a sua Opcao")

    desenvolva um programa que faça 3 perguntas

"""


"""MAIS UM EXERCICIO DE LOGICA USANDO WHILE E IF, ELIF E ELSE

ver = "v"
f = "f"
resposta = "v"
errada = "f"
opcao = 0
continuar_jogo = True

print("====================BEM-VINDO AO JOGO VERDADEIRO OU FALSO====================")

while continuar_jogo:
    print("Real Madrid foi campeão da Champions League de 2008? Verdadeiro (v) ou Falso (f)?")
    opcao = input("-----> ")
    if opcao == f:
        print("Parabéns, você acertou!")

        print("=====PROXIMA PERGUNTA=====")
        print("FLAMENGO JÁ CAIU DE DIVISÃO DO CAMPEONATO BRASILEIRO? (v) OU (f)FALSO? ")
        opcao = input("-----> ")
        if opcao == f:
            print("Parabens voce acertou novamente.")
            continuar_jogo = True
        elif opcao == ver:
            print("Ops, você errou. Tente novamente.")
            continuar_jogo = False

        print("=====PROXIMA PERGUNTA=====")

        print("Benfica é o melhor clube de portugal (v) ou (f) falso? ")
        opcao = input("-----> ")
        if opcao == f:
            print("Parabens voce acertou novamente.")
        elif opcao == ver:
            print("Ops, você errou. Tente novamente.")
        continuar_jogo = False
    else:
        print("Opção inválida. Por favor, escolha Verdadeiro (v) ou Falso (f).")

"""



"""
CRIE O JOGO DA ADIVINHA O CPU DEVE PENSAR NUM NUMERO DE 0 A 10 E O UTILIZADRO DEVE ADIVINHAR O NUMERO ESCOLHIDO.
SÓ QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATÉ ACERTAR.
NO FINAL MOSTRE QUANTAS TENTATIVAS FORAM NECESSARIAS. 
"""


"""
import random

numeros_possiveis = list(range(1, 11))

numero_cpu = random.choice(numeros_possiveis)
tentativas = 0

print("====== BEM-VINDO AO JOGO DE ADIVINHAÇÃO ======")


while True:
    tentativa_jogador = int(input("Escolha um número de 1 a 10: "))
    tentativas += 1

    if tentativa_jogador == numero_cpu:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    else:
        print("Ops, você errou. Tente novamente.")

ver = "v"
f = "f"
continuar_jogo = True

print("====================BEM-VINDO AO JOGO VERDADEIRO OU FALSO====================")

while continuar_jogo:
    print("Real Madrid foi campeão da Champions League de 2008? Verdadeiro (v) ou Falso (f)?")
    opcao = input("-----> ").lower()
    if opcao not in [ver, f]:
        print("Opção inválida. Por favor, escolha Verdadeiro (v) ou Falso (f).")
        continue

    if opcao == f:
        print("Parabéns, você acertou!")
    else:
        print("Ops, você errou. Tente novamente.")
        break

    print("=====PROXIMA PERGUNTA=====")
    print("FLAMENGO JÁ CAIU DE DIVISÃO DO CAMPEONATO BRASILEIRO? Verdadeiro (v) ou Falso (f)? ")
    opcao = input("-----> ").lower()
    if opcao not in [ver, f]:
        print("Opção inválida. Por favor, escolha Verdadeiro (v) ou Falso (f).")
        continue

    if opcao == f:
        print("Parabéns, você acertou novamente.")
    else:
        print("Ops, você errou. Tente novamente.")
        break

    continuar_jogo = False

print("Obrigado por jogar!")


opcao = 0

while opcao != 4:
    print("[ 1 ] - Regstar pessoa")
    print("[ 2 ] - Nº Pessoas registadas")
    print("[ 3 ] - Apagar um registo")
    print("[ 4 ] - Sair")
    print("Qual a sua opção")
    opcao = int(input("-----> "))
    if opcao == 1:
        nome = input("Digite o nome da pessoa")
        idade = int(input("Digite a idade da pessoa"))
        print(f"{nome} registado com sucesso.")
    elif opcao == 2:
        print("Há X pessoas registadas")
    elif opcao == 3:
        print("Um registo foi apagado!")
    elif opcao < 1 or opcao > 4:
        break
    elif opcao == 4:
        break
print("Obrigado e volte sempre!")
"""


"""
preço = float(input("Qual é o preço do produto ? € "))
novo = preço - (preço * 5 / 100)
print(f" o Produto que Custava €{preço}, na promoção black Friday de 5% vai custa €{novo}")



salario = float(input("Qual o valor do seu salario € ? "))
novo = salario + (salario * 10 / 100)
print(f"o Salario do fucionario pika teve o aumento de {novo}")

"""


"""

dias = int(input("Quantos dias Alugados ? "))
km = float(input("Quantos Km rodados ? "))
pago = (dias * 60) + (km * 0.15)
print(f" O total a pagar é de € {pago} ")

"""

resposta_certa
resposta_errada
S

print("==========QUIZ DO FUTEBOL==========")

print("Deseja jogar Digite S para Sim")
    if S == S:
        else
        print("Vamos ao Jogo!")



















