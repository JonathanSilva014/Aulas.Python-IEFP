class ContaBancaria:
    def __init__(self, nib, titular, saldo, limite):
        self.__nib = nib
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def get_nib(self):
        return self.__nib
    
    def set_nib(self, novo_nib):
        self.__nib = novo_nib
        
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, novo_saldo):
        self.__saldo = novo_saldo
        
    def get_limite(self):
        return self.__limite
    
    def set_limite(self, novo_limite):
        self.__limite = novo_limite
        
    def get_titular(self):
        return self.__titular
    
    def set_titular(self, novo_titular):
        self.__titular = novo_titular

# Solicitar informações do usuário
nib = input("Digite o NIB: ")
titular = input("Digite o titular: ")
saldo = float(input("Digite o saldo: "))
limite = float(input("Digite o limite: "))

# Criar uma instância da classe com as informações fornecidas pelo usuário
conta = ContaBancaria(nib=nib, titular=titular, saldo=saldo, limite=limite)

# Exibir informações da conta
print(f"\nInformações da conta:")
print(f"NIB: {conta.get_nib()}")
print(f"Titular: {conta.get_titular()}")
print(f"Saldo: {conta.get_saldo()}")
print(f"Limite: {conta.get_limite()}")
