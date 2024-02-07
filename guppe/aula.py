"""# Ex1
print("Hello world")


# Ex2
print("------------------------------------")
print("------<Welcome to my software>------")
print("------------------------------------")


# Ex3
num1 = int(input("Please write 1º number: "))
num2 = int(input("Please write 2º number: "))
result = num1 + num2

print("The sum of", num1, "and", num2, "is", result, "\n")
                                                    # ^ this means it can have paragraph use "\" for this context
                                                    # There are others types:
                                                      # \a can give alert sound effect
                                                      #


# Ex4
num = int(input("Please write the number: "))
num_plus = num + 1
num_Minos = num - 1

print("The number next of", num, "is", num_plus)
print("The number next of", num, "is", num_Minos)
"""
import time

"""# Ex5
# read the output of the user
num1 = int(input("Please write 1st number: "))
num2 = int(input("Please write 2nd number: "))

# Define the variables and do math of the output that was introduced by user
num_add = num1 + num2
num_minus = num1 - num2
num_multi = num1 * num2
num_div = num1 // num2
num_rest = num1 % num2

# read the output of the user
print("The results from", num1, "and", num2, "are:")
print("Will Add to", num_add)
print("Will Subtracted to", num_minus)
print("Will Multiple to", num_multi)
print("Will Divided to", num_div)
print("Will Rest Divided to", num_rest)"""

"""# Ex6
# read the output of the user
num1 = float(input("Please write 1st number: "))
num2 = float(input("Please write 2nd number: "))
num3 = float(input("Please write 3th number: "))
num4 = float(input("Please write 4th number: "))
num5 = float(input("Please write 5th number: "))

# Define the variables and do math of the output that was introduced by user
average = (num1 + num2 + num3 + num4 + num5) / 5

# Read the results to screen
print("The average is ", average)"""

"""
""# Ex7
# read the output of the user
name = input("Please Insert ur name: ")
birth_year = int(input("Please Insert ur Birth year: "))
current_year = int(input("Please Insert the current year: "))

# Define the variables and do math of the output that was introduced by user
age = current_year - birth_year

# Read the results to screen
print("Hi", name, "you are", age, "years old")

# Ex8
# read the output of the user
km = float(input("Insira o KM que o carro rodou: "))
rent_days = int(input("Insira os dias em que o carro foi alugado: "))

# Definir constantes
PRICE_KM = 0.456  # Corrigi a vírgula para um ponto
PRICE_RENT_DAYS = 60

# Defina as variáveis e faça as contas da saída que foi introduzida pelo usuário
total_km = km * PRICE_KM
total_rent_days = rent_days * PRICE_RENT_DAYS

# Leia os resultados na tela
total_cheio = total_km + total_rent_days
print("O total seria", total_cheio, "Euros", "de", total_km, "para km e", total_rent_days, "para o aluguel")
print("Você correu", km, "km e alugou por", rent_days, "dias")
"""

"""
nome = input("Qual seu nome? ")
idade = int(input("Qual a sua idade? "))

print(f"{nome}, é um cara muito legal, e tem, {idade} anos.")
"""

"""
frase = ("Curso de Python")
print(frase.replace("Python", "C++"))
"""

"""
lower == tudo minusculo
upper == tudo maiusculo

"""

"""
frase = input("Digite seu Nome Completo ").strip()
print(frase.upper())

print("=============")

frase1 = ("Agora com letras Pequenas.")
print(frase1)
print("=============")
print(frase.lower())

print("=============")

frase2 = ("E Por ultimo a quantidade de caracteres.")
print(frase2)
print(len(frase))

pFrase = frase.split()
print("O seu primeiro nome é {} e tem {} caractere".format(pFrase[0], len(pFrase)))

"""


"""nome = input("Digite o seu nome completo: ").strip()
print("Vamos Analisar seu Nome Campeão....")

print("=====================")

print("Seu Nome em Letras Maiusculas")
print(format(nome.upper()))

print("=====================")

print("Seu Nome em Letras pequenas")
print(format(nome.lower()))

print("=====================")

print("Seu Nome em tem {} caracteres".format(len(nome) - nome.count(" ")))

pNome = nome.split()

print("Então Campeão seu Primeiro nome é {} e tem {} caracteres".format(pNome[0], len(pNome[0])))
"""

"""
num = int(input("Digite um numero de 0 a 9999 "))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

"""

"""
frase = input("digite a frase ").strip()
print("A letra A aparece {} vezes. " .format(frase.count("A")))
print("O Primeiro A aparece na posição {} . " .format(frase.find("A")))
print("O ultimo A aparece na posição {}. " .format(frase.rfind(A+1)))
"""

"""
frase = input("Digite a frase: ").strip()

# Convertendo a frase para minúsculas
frase_minuscula = frase.lower()

# Contagem de ocorrências do caractere "a"
ocorrencias_a = frase_minuscula.count("a")

print("A letra 'A' aparece {} vezes.".format(ocorrencias_a))

# Encontrar a posição do primeiro "A"
posicao_primeiro_a = frase.find("A")
print("O primeiro 'A' aparece na posição {}.".format(posicao_primeiro_a))

# Encontrar a posição do último "A"
posicao_ultimo_a = frase.rfind("A")
print("O último 'A' aparece na posição {}.".format(posicao_ultimo_a))
"""

"""
nome = input("Qual seu nome completo ? ")

print("ola ", nome, "o seu registo esta completo ")
print("O seu emal é ",nome,"@empresa.pt")
print("Email:")
"""

"""
nome = input(" Qual é o seu primeiro nome ?")
seg_nome = input(" Qual é o seu segundo nome ?")

print("Seu nome todo é ", nome + seg_nome)
"""

"""
palavra = input("Palavra com até 6 letras")

print(palavra[::-1])
"""


"""
idade = int(input("Qual sua idade? "))

if idade < 18:
    print("Menor de idade")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")

"""
"""
print("=====RADAR DE VELOCIDADE======")

velocidade = int(input("Qual a sua Velociade? "))
multa = (velocidade - 80) * 7 + 100

if velocidade <= 80:
    print("Boa Viagem")
elif velocidade > 80:
    print("Infelizmente o senhor foi Multado! ", multa,"€")

"""

"""
print("======Par ou Impar=======")

num = int(input("Qual numero deseja inserir :" ))

if num % 2 == 0:
    print(f"{num} é um número par.")
else:
    print(f"{num} é um número ímpar.")
"""

"""
print("======NOTAS DO SEMESTRE=======")

nota1 = float(input("Digite a Primeira nota do Aluno "))
nota2 = float(input("Digite a Segunda nota do Aluno "))
nota3 = float(input("Digite a Terceira nota do Aluno "))
nota4 = float(input("Digite a Quarta nota do Aluno "))
nota5 = float(input("Digite a Quinta nota do Aluno "))

soma_notas = nota1 + nota2 + nota3 + nota4 + nota5
media = soma_notas / 5

print(f"A média do aluno é: {media:.2f}")

if media >= 9.5:
    print("Passou, parabéns!")
elif 8 < media < 9.5:
    print("Recuperação, Estude mais um pouco")
else:
    print("Reprovado, Vai ter que Repetir o Semestre")
"""

"""
print("==========BASE DE CONVERSÃO==========")

numero = int(input("Digite um numero: "))

print("Deseja converter para que tipo ? ")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")

opcao = int(input("Digite o número da opção desejada: "))

if opcao == 1:
    print(f"O Numero {numero} em Binario é : {bin(numero)[2:1]}")
elif opcao == 2:
    print(f"O Numero {numero} em octal é : {oct(numero)[2:1]}")
elif opcao == 3:
    print(f"O Numero {numero} em octal é : {hex(numero)[2:1]}")
else:
    print("Tente novamente Opção invalida")

"""

"""
print("===== DOIS NÚMEROS =====")

numero = int(input("Digite o primeiro número: "))
numero1 = int(input("Digite o segundo número: "))

if numero > numero1:
    print(f"O número {numero} é maior do que o número {numero1}")
elif numero1 > numero:  # Corrigido aqui
    print(f"O número {numero1} é maior que o número {numero}")
else:
    print("Os números são iguais.")
"""

"""
import random
import time

numeros = random.randint(0, 7)

# Escolha do número pela parte do utilizador
numeroEscolhido = int(input('Estou a pensar num número de 0 a 7, consegues adivinhar?  '))

print("Hmm....")
time.sleep(2)
print("....")
time.sleep(2)

# Condição para verificar se o utilizador escolheu o número certo
if numeroEscolhido == numeros:
    print(f"Acertaste! O número que eu pensei era {numeros}")
else:
    print(f"Perdeste :(, eu escolhi {numeros} e tu disseste {numeroEscolhido}")
"""

import random
import time

print("Bem-Vindo ao jogo Pedra, Papel e Tesousa.")
print("Escolha um entre os tres para iniciaziar a partida.")

pedra = 1
papel = 2
tesoura = 3

print("Pedra [ 1 ]")
print("Papel [ 2 ]")
print("Tesoura [ 3 ]")

resultado = int(input("Digite uma Jogada "))

print("Aguardado Resultado do seu Adversario...")
time.sleep(2)

adversario = random.randint(1, 3)

if resultado == 1:
    print("Você escolheu Pedra.")
    if adversario == 1:
        print("Seu adversário escolheu Pedra. Empate!")
    elif adversario == 2:
        print("Seu adversário escolheu Papel. Você perdeu!")
    else:

if resultado == 2:
    print("Você escolheu Papel.")
    if adversario == 2:
        print("Seu adversario escolheu Papel. Você Empatou")
    elif adversario == 3:
        print("Seu adversário escolheu Papel. Você Perdeu!")
    else:









