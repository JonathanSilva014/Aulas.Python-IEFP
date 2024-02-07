"""

import time

print("==========BEM-VINDO À FARMÁCIA PYTHON==========")
print("Vamos verificar primeiramente o seu peso")

peso = int(input("Digite o Seu peso: "))
altura = float(input("Digite a Sua Altura: "))

print("Calculando...")
time.sleep(0.5)
print("... Farmacia Python trazendo saude a você.")
time.sleep(2.0)

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Seu IMC é de {imc:.1f}. Infelizmente, você está abaixo do peso. Tente comer mais, por gentileza.")
elif 18.5 <= imc <= 24.9:
    print(f"Seu IMC é de {imc:.1f}. Você está no peso ideal. Continue assim e beba água.")
elif 25.0 <= imc <= 29.9:
    print(f"Seu IMC é de {imc:.1f}. Você está com sobrepeso.")
elif 30.0 <= imc <= 34.9:
    print(f"Seu IMC é de {imc:.1f}. Obesidade Grau 1, procure fazer caminhadas e cuide de sua saúde.")
elif 35.0 <= imc <= 39.9:
    print(f"Seu IMC é de {imc:.1f}. Obesidade Grau 2. Considere treinar mais, beber mais água e fazer caminhadas. Cuide de sua saúde.")
elif imc >= 40.0:
    print(f"Seu IMC é de {imc:.1f}. Obesidade Grau 3 Morbida. Considere treinar mais, beber mais água e fazer caminhadas. Cuide de sua saúde.")
"""





