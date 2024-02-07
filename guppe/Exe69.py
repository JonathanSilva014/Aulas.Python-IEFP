def calcular_imc(altura_pessoa, peso_pessoa):
    imc = peso_pessoa / (altura_pessoa ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        print("Você está abaixo do peso, faça um favor de se alimentar mais.")
    elif 18.5 <= imc < 24.9:
        print("Você está com peso adequado e normal, mantenha-se assim.")
    elif 25 <= imc < 29.9:
        print("Você está com um pouco de sobrepeso, tome cuidado.")
    elif 30 <= imc < 34.9:
        print("Você está com obesidade Grau 1, tome cuidado e faça exercícios para se manter em forma.")
    elif 35 <= imc < 39.9:
        print("Você está com obesidade Grau 2, tome cuidado e faça exercícios para se manter em forma.")
    else:
        print("Você está com obesidade Grau 3, tome cuidado e faça exercícios para se manter em forma.")

def main():
    print("==========MEDIDOR DE IMC==========")
    altura_pessoa = float(input("Qual a sua altura em metros? "))
    peso_pessoa = float(input("Qual o seu peso em quilogramas? "))

    imc = calcular_imc(altura_pessoa, peso_pessoa)

    print(f"Seu IMC é: {imc}")
    classificar_imc(imc)

if __name__ == "__main__":
    main()
