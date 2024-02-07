class Personagem:
    def __init__(self, nome):
        self._nome = nome
        self._vida = 100
        self._experiencia = 0
        self._poderes = 1
        self._nivel = 1
        
    @property
    def nome(self):
        return f'Personagem: {self._nome}'
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
        
    @property
    def vida(self):
        return f'Pontos vitais: {self._vida}'

    @property
    def experiencia(self):
        return f'XP: {self._experiencia}'

# Criar uma instância da classe corretamente
novo_personagem = Personagem("Jonathan")
print(novo_personagem.nome)

# Alterar o nome usando o setter
novo_personagem.nome = "Alfredo"
print(novo_personagem.nome)
