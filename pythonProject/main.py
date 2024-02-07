if __name__ == '__main__':
    print("Qual o peso em Kg ? ")
    peso = float(input())

    print("Qual a sua Altura em Metros ? ")
    altu = float(input())

    print("Qual a idade ? ")
    ida = int(input())

    taxaM = 665 + 9.6 * peso + 1.8 * altu + 4.7 * ida

    print("Taxa de Metabolismo = ", taxaM)
