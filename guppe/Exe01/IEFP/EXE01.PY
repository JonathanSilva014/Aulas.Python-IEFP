"""Crie uma classe Livro com atributos privados titulo, autor, ano de publicação. 
Utilize getterse setters para aceder e modificar estes atributos. 
Os setters devem garantir que tanto
o título quanto o nome do autor sejam strings não vazias e que o ano seja num intervalo 
razoável entre 1900 e o ano atual."""

"""PARTE 2"""

"""Modifique a classe Livro do Exercício 1 e implemente o método __str__ para que, ao 
imprimir um objeto Livro, apareça uma stringno 
formato: Título: [titulo] 
Autor: [autor] 
Ano: [ano]"""

from datetime import date

# FIZ IMPORT DAS DATAS

class Livro:
    def __init__(self, titulo, autor, ano_publicado):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicado = ano_publicado

    @property #ESSES SÃO OS GET E SET DE TITULO
    def titulo(self):
        return self.__titulo

    @titulo.setter 
    def titulo(self, novo_titulo):
        if isinstance(novo_titulo, str) and novo_titulo != "":
            self.__titulo = novo_titulo
        else:
            print("Título inválido. Deve ser uma string não vazia.")

    @property # ESSES SÃO OS GET E SETTER DO AUTOR 
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, novo_autor):
        if isinstance(novo_autor, str) and novo_autor != "":
            self.__autor = novo_autor
        else:
            print("Autor inválido. Deve ser uma string não vazia.")

    @property # ESSES SÃO OS GET E SETTER DO ANO_PUBLICADO
    def ano_publicado(self):
        return self.__ano_publicado

    @ano_publicado.setter
    def ano_publicado(self, novo_ano):
        ano_atual = date.today().year
        if isinstance(novo_ano, int) and 1900 <= novo_ano <= ano_atual:
            self.__ano_publicado = novo_ano
        else:
            print("Ano de publicação inválido. Deve estar no intervalo entre 1900 e o ano atual.")
    
    def __str__(self):
        return f"Título: {self.__titulo}\nAutor: {self.__autor}\nAno: {self.__ano_publicado}"

def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar Livro")
    print("2. Modificar Livro")
    print("0. Sair")
    
def modificar_livro(livros):
    if not livros:
        print("Não há livros para modificar.")
        return

    print("Lista de Livros:")
    for i, livro in enumerate(livros, start=1):
        print(f"{i}. {livro.titulo} - {livro.autor} - {livro.ano_publicado}")

    # Solicitar ao usuário qual livro deseja modificar
    while True:
        try:
            escolha = int(input("Digite o número do livro que deseja modificar (0 para cancelar): "))
            if 0 <= escolha <= len(livros):
                break
            else:
                print("Escolha inválida. Digite um número válido.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    if escolha == 0:
        print("Operação de modificação cancelada.")
        return

    # Obtendo o índice correto na lista (subtraindo 1 por causa da indexação baseada em zero)
    indice_livro = escolha - 1
    livro_selecionado = livros[indice_livro]

    # Exibir informações do livro selecionado
    print("\nLivro Selecionado:")
    print(f"Título: {livro_selecionado.titulo}")
    print(f"Autor: {livro_selecionado.autor}")
    print(f"Ano de Publicação: {livro_selecionado.ano_publicado}")

    # Solicitar ao usuário as modificações desejadas
    novo_titulo = input("Digite o novo título (deixe em branco para manter o atual): ")
    novo_autor = input("Digite o novo autor (deixe em branco para manter o atual): ")

    while True:
        try:
            novo_ano = int(input("Digite o novo ano de publicação (deixe em branco para manter o atual): "))
            break
        except ValueError:
            print("Ano inválido. Digite um número inteiro.")

    # Aplicar as modificações
    if novo_titulo:
        livro_selecionado.titulo = novo_titulo
    if novo_autor:
        livro_selecionado.autor = novo_autor
    if novo_ano:
        livro_selecionado.ano_publicado = novo_ano

    print("Livro modificado com sucesso!")

def main():
    livros = []  # Lista para armazenar os livros

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            # Adicionar Livro
            titulo_input = input("Digite o título do livro: ")
            autor_input = input("Digite o nome do autor: ")

            while True:
                try:
                    ano_input = int(input("Digite o ano de publicação: "))
                    break
                except ValueError:
                    print("Ano inválido. Digite um número inteiro.")

            novo_livro = Livro(titulo_input, autor_input, ano_input)
            livros.append(novo_livro)
            print("Livro adicionado com sucesso!")

        elif escolha == "2":
            modificar_livro(livros)

        elif escolha == "0":
           
            break

        else:
            print("Opção inválida. Tente novamente.")
    




         