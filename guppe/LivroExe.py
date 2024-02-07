class Livro:
    def __init__(self):
        self.__titulo = ""
        self.__ano = ""
        self.__autor = ""
        self.__disponibilidade = False

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = autor


print("== Biblioteca ==")
asd = input("Clique ENTER para adicionar um novo livro...")
titulo = input("TITULO: ")
ano = int(input("ANO: "))
autor = input("AUTOR: ")
disbonibilidade = input("DISPONIBILIDADE [s/n] : ").strip().lower()
if disbonibilidade == "s":
    disbonibilidade = True
else:
    disbonibilidade = False

livro = Livro()
livro.titulo = titulo
livro.ano = ano
livro.autor = autor
livro.disponibilidade = disbonibilidade

print(f"\nInformações do Livro:")
print(f"Titulo: {livro.titulo}")
print(f"Ano: {livro.ano}")
print(f"Autor: {livro.autor}")
print(f"Disponibilidade: {livro.disponibilidade}")