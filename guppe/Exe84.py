class Temperatura:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @property
    def kelvin(self):
        return self._celsius + 273.15

# Exemplo de uso
temperatura_atual = Temperatura(25)

print(f'Temperatura em Celsius: {temperatura_atual.celsius}°C')
print(f'Temperatura em Fahrenheit: {temperatura_atual.fahrenheit}°F')
print(f'Temperatura em Kelvin: {temperatura_atual.kelvin}K')

# Alterando a temperatura em Celsius
temperatura_atual.celsius = 30

# Exibindo os novos valores
print(f'Nova temperatura em Celsius: {temperatura_atual.celsius}°C')
print(f'Nova temperatura em Fahrenheit: {temperatura_atual.fahrenheit}°F')
print(f'Nova temperatura em Kelvin: {temperatura_atual.kelvin}K')
