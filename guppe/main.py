from crud.adicionar import adicionar_livro
from crud.devolver import devolucao_livro
from crud.emprestar import emprestar_livro5
from crud.listar import listagem
from crud.pesquisar import pesquisa
from crud.remover import apagar_livro

# Menu do programa
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
            apagar_livro()

        elif opcao == "3":
            listagem()

        elif opcao == "4":
            pesquisa()

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
