livros = []
livro = {
    "Título": ['A Casa de Papel', 'A CASA', 'LISBOA LINDA', 'BENFICA', 'A BRUXA', 'ZEUS', 'HARRY POTTER', 'SENHORES DOS ANEIS', 'CARROS'],
    "Autor": ['FOX', 'ACER', 'FOXX1', 'LENDARIOS', 'FANCHET', 'REALEZA', 'JOGA', 'LISA', 'KIL'],
    "ISBN": ['12547', '14785', '1025', '1010101', '789610', '9978', '123456', '1478', '036987'],
    "Ano de Publicação": ['2004', '1994', '1995', '2010', '1990', '2002', '1998', '2001', '2014'],
    "Editora": ['FOX', 'ACER', 'FOXX1', 'LENDARIOS', 'FANCHET', 'REALEZA', 'JOGA', 'LISA', 'KIL'],
    "Categoria ou Gênero": ['AÇÃO', 'DRAMA', 'COMEDIA', 'DRAMA', 'ROMANCE', 'SUSPENSE', 'COMEDIA', 'TERROR', 'TERROR'],
    "Status de Disponibilidade": ['Disponível','Disponível','Disponível','Disponível','INDISPONIVEL','Disponível','Disponível','Disponível','Disponível'],
    "Emprestado para": ['Ninguém','Ninguém','Ninguém','Ninguém','Alguem','Ninguém','Ninguém','Ninguém','Ninguém'],
    "Data de Devolução": None
}

biblioteca = [
    {"Título": 'A Casa de Papel', "Autor": 'FOX', "ISBN": '12547', "Ano de Publicação": '2004', "Editora": 'FOX', "Categoria ou Gênero": 'AÇÃO', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém', "Data de Devolução": None},
    {"Título": 'A CASA', "Autor": 'ACER', "ISBN": '14785', "Ano de Publicação": '1994', "Editora": 'ACER', "Categoria ou Gênero": 'DRAMA', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém', "Data de Devolução": None},
    {"Título": 'LISBOA LINDA', "Autor": 'GIGA', "ISBN": '5247', "Ano de Publicação": '1995', "Editora": 'FOXX1', "Categoria ou Gênero": 'COMEDIA', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém', "Data de Devolução": None},
    {"Título": 'O LOBO MAL', "Autor": 'LOUÇA', "ISBN": '9852', "Ano de Publicação": '2004', "Editora": 'FOX', "Categoria ou Gênero": 'AÇÃO', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém', "Data de Devolução": None},
    {"Título": 'SURFISTINHA', "Autor": 'ACER', "ISBN": '9854', "Ano de Publicação": '1994', "Editora": 'ACER', "Categoria ou Gênero": 'DRAMA', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém', "Data de Devolução": None},
    {"Título": 'O PINTO DA COSTA', "Autor": 'FOXX1', "ISBN": '1025', "Ano de Publicação": '1995', "Editora": 'FOXX1', "Categoria ou Gênero": 'COMEDIA', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém', "Data de Devolução": None},
    {"Título": 'O PORTO', "Autor": 'FOX', "ISBN": '12547', "Ano de Publicação": '2004', "Editora": 'FOX', "Categoria ou Gênero": 'AÇÃO', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém', "Data de Devolução": None},
    {"Título": 'LIMBO FEROZ', "Autor": 'LONG', "ISBN": '14785', "Ano de Publicação": '1994', "Editora": 'ACER', "Categoria ou Gênero": 'DRAMA', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém', "Data de Devolução": None},
    {"Título": 'PYTHON', "Autor": 'FOX2', "ISBN": '85214', "Ano de Publicação": '1995', "Editora": 'FOXX1', "Categoria ou Gênero": 'COMEDIA', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém', "Data de Devolução": None},
    {"Título": 'JAVA', "Autor": 'GIGA', "ISBN": '12547', "Ano de Publicação": '2004', "Editora": 'FOX', "Categoria ou Gênero": 'AÇÃO', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém', "Data de Devolução": None},
    {"Título": 'LIVRO DE COZINHA', "Autor": 'PIA', "ISBN": '14785', "Ano de Publicação": '1994', "Editora": 'ACER', "Categoria ou Gênero": 'DRAMA', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém', "Data de Devolução": None},
    {"Título": 'CULINARIA AFRICANA', "Autor": 'KIA', "ISBN": '85236', "Ano de Publicação": '1995', "Editora": 'FOXX1', "Categoria ou Gênero": 'COMEDIA', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém', "Data de Devolução": None},
    {"Título": 'O VERÃO PASSADO', "Autor": 'KA', "ISBN": '125477', "Ano de Publicação": '2004', "Editora": 'FOX', "Categoria ou Gênero": 'AÇÃO', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém', "Data de Devolução": None},
    {"Título": 'EFEITOS DE DIREITO', "Autor": 'ACER', "ISBN": '1478547', "Ano de Publicação": '1994', "Editora": 'ACER', "Categoria ou Gênero": 'DRAMA', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém', "Data de Devolução": None},
    {"Título": 'O ADVOGADO', "Autor": 'FOX', "ISBN": '1025417', "Ano de Publicação": '1995', "Editora": 'FOXX1', "Categoria ou Gênero": 'COMEDIA', "Status de Disponibilidade": 'Disponível', "Emprestado para": 'Ninguém', "Data de Devolução": None},
]

def adicionar_livro():
    titulo = input("Título do Livro: ")
    autor = input("Autor(es): ")
    isbn = input("ISBN: ")
    ano_publicacao = input("Ano de Publicação: ")
    editora = input("Editora: ")
    categoria = input("Categoria ou Gênero: ")

    novo_livro = {
        "Título": titulo,
        "Autor": autor,
        "ISBN": isbn,
        "Ano de Publicação": ano_publicacao,
        "Editora": editora,
        "Categoria ou Gênero": categoria,
        "Status de Disponibilidade": "Disponível",
        "Emprestado para": None,
        "Data de Devolução": None
    }

    biblioteca.append(novo_livro)
    print("Livro adicionado com sucesso!")

def listar_livros():
    print("\nLista de Livros:")
    for livro in biblioteca:
        print("\nTítulo:", livro["Título"])
        print("Autor:", livro["Autor"])
        print("ISBN:", livro["ISBN"])
        print("Ano de Publicação:", livro["Ano de Publicação"])
        print("Editora:", livro["Editora"])
        print("Categoria ou Gênero:", livro["Categoria ou Gênero"])
        print("Status de Disponibilidade:", livro["Status de Disponibilidade"])
        print("Emprestado para:", livro["Emprestado para"])
        print("Data de Devolução:", livro["Data de Devolução"])

def remover_livro():
    isbn_a_remover = input("Digite o ISBN do livro a ser removido: ")
    for livro in biblioteca:
        if livro["ISBN"] == isbn_a_remover:
            biblioteca.remove(livro)
            print("Livro removido com sucesso!")
            return
    print("Livro não encontrado.")

def procurar_livros():
    termo_busca = input("Digite um termo para buscar livros: ")
    termo_lower = termo_busca.lower()
    resultados = []
    for livro in biblioteca:
        if termo_lower in livro["Título"].lower() or termo_lower in livro["Autor"].lower():
            resultados.append(livro)

    if resultados:
        print("\nResultados da busca:")
        for livro in resultados:
            print("Título:", livro["Título"])
            print("Autor:", livro["Autor"])
            print("ISBN:", livro["ISBN"])
            print("Ano de Publicação:", livro["Ano de Publicação"])
            print("Editora:", livro["Editora"])
            print("Categoria ou Gênero:", livro["Categoria ou Gênero"])
            print("Status de Disponibilidade:", livro["Status de Disponibilidade"])
            print("Emprestado para:", livro["Emprestado para"])
            print("Data de Devolução:", livro["Data de Devolução"])
    else:
        print("Nenhum livro encontrado.")

def emprestar_livro():
    isbn_emprestimo = input("Digite o ISBN do livro a ser emprestado: ")
    for livro in biblioteca:
        if livro["ISBN"] == isbn_emprestimo and livro["Status de Disponibilidade"] == "Disponível":
            livro["Status de Disponibilidade"] = "Indisponível"
            livro["Emprestado para"] = input("Nome da pessoa que está pegando emprestado: ")
            livro["Data de Devolução"] = input("Data prevista de devolução: ")
            print("Livro emprestado com sucesso!")
            return
        elif livro["ISBN"] == isbn_emprestimo and livro["Status de Disponibilidade"] == "Indisponível":
            print("O livro não está disponível no momento.")
            return
    print("Livro não encontrado.")

def devolucao_livro():
    isbn_devolucao = input("Digite o ISBN do livro a ser devolvido: ")
    for livro in biblioteca:
        if livro["ISBN"] == isbn_devolucao and livro["Status de Disponibilidade"] == "Indisponível":
            livro["Status de Disponibilidade"] = "Disponível"
            livro["Emprestado para"] = None
            livro["Data de Devolução"] = None
            print("Livro devolvido com sucesso!")
            return
        elif livro["ISBN"] == isbn_devolucao and livro["Status de Disponibilidade"] == "Disponível":
            print("Este livro não estava emprestado.")
            return
    print("Livro não encontrado.")

# Loop principal do programa
while True:
    print("[ 1 ] - Adicionar Livro")
    print("[ 2 ] - Remover Livro")
    print("[ 3 ] - Listar Livros")
    print("[ 4 ] - Procurar Livro")
    print("[ 5 ] - Emprestar Livro")
    print("[ 6 ] - Devolver Livro")
    print("[ 0 ] - Sair")

    try:
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_livro()

        elif opcao == "2":
            remover_livro()

        elif opcao == "3":
            listar_livros()

        elif opcao == "4":
            procurar_livros()

        elif opcao == "5":
            emprestar_livro()

        elif opcao == "6":
            devolucao_livro()

        elif opcao == "0":
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")



import pyautogui









