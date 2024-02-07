def verificar_carta(ano_nascimento):
    """
    Esta função verifica se a pessoa pode tirar a carta de condução com base no ano de nascimento.
    """
    idade = 2024 - ano_nascimento

    if idade >= 18:
        print(f"A pessoa que nasceu no ano de {ano_nascimento} pode tirar a carta de condução.")
    elif 16 <= idade < 18:
        print(f"A pessoa que nasceu no ano de {ano_nascimento} não pode tirar a carta de condução sem a autorização do encarregado de educação.")
    else:
        print(f"A pessoa que nasceu no ano de {ano_nascimento} não pode tirar a carta de condução.")

def main():
    print("==========CARTA DE CONDUÇÃO==========")
    ano_nascimento = int(input("Em que ano o Senhor ou a Senhora nasceu? "))
    verificar_carta(ano_nascimento)

if __name__ == "__main__":
    main()
