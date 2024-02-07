import math

class Circulo:
    def __init__(self, raio):
        print("Construindo objeto...")
        self.__raio = raio
        self.__area = None  # Inicializamos como None e calcularemos quando necessário
        self.__perimetro = None  # Inicializamos como None e calcularemos quando necessário
        
    def get_raio(self):
        return f"O raio do círculo é {self.__raio}"
    
    def set_raio(self, raio):
        print("Definindo novo raio...")
        self.__raio = raio
        # Se o raio foi alterado, resetamos a área e o perímetro para None
        self.__area = None
        self.__perimetro = None

    def calcular_area(self): 
        if self.__area is None:
            self.__area = math.pi * self.__raio**2
        return self.__area

    def calcular_perimetro(self):
        if self.__perimetro is None:
            self.__perimetro = 2 * math.pi * self.__raio
        return self.__perimetro

# Exemplo de uso da classe
raio_circulo = 5
circulo = Circulo(raio_circulo)

# Exibindo o raio
print(circulo.get_raio())

# Calculando e exibindo a área
area = circulo.calcular_area()
print(f"Área do círculo: {area:.2f}")

# Calculando e exibindo o perímetro
perimetro = circulo.calcular_perimetro()
print(f"Perímetro do círculo: {perimetro:.2f}")

# Alterando o raio
novo_raio = 8
circulo.set_raio(novo_raio)

# Exibindo o novo raio
print(circulo.get_raio())

# Calculando e exibindo a nova área
nova_area = circulo.calcular_area()
print(f"Nova área do círculo: {nova_area:.2f}")

# Calculando e exibindo o novo perímetro
novo_perimetro = circulo.calcular_perimetro()
print(f"Novo perímetro do círculo: {novo_perimetro:.2f}")
