def analisar_notas(notas):
    """
    Esta função recebe uma lista de notas de alunos e retorna um dicionário com informações sobre as notas.
    """
    quantidade_notas = len(notas)

    if quantidade_notas == 0:
        return {"mensagem": "Nenhuma nota fornecida."}

    maior_nota = max(notas)
    media_turma = sum(notas) / quantidade_notas

    situacao = ""
    if media_turma > 12:
        situacao = "Boa"
    elif media_turma < 9.5:
        situacao = "Fraca"
    else:
        situacao = "Razoável"

    resultado = {
        "quantidade_notas": quantidade_notas,
        "maior_nota": maior_nota,
        "media_turma": media_turma,
        "situacao": situacao
    }

    return resultado


def main():
    print("========== ANÁLISE DE NOTAS DOS ALUNOS ==========")

    # Solicitar as notas dos alunos
    notas_str = input("Digite as notas dos alunos separadas por espaços (ex: 10 12 15): ")

    # Converter as notas para uma lista de floats
    notas = [float(nota) for nota in notas_str.split()]

    # Chamar a função para analisar as notas
    resultado_analise = analisar_notas(notas)

    # Imprimir os resultados
    print("\nResultados da análise:")
    for chave, valor in resultado_analise.items():
        print(f"{chave}: {valor}")


if __name__ == "__main__":
    main()
