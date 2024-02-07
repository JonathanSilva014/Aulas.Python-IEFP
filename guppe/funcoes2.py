def soma(a, b):
    """
    -> Esta função imprime no ecrã a soma entre as variáveis.
    :param a: primeiro número
    :param b: segundo número
    :return: None
    """
    s = a + b
    print(f"A soma entre {a} e {b} é igual a {s}")

soma(10, 15)
print("~~" * 10)
print("Utilizar help")
help(soma)

def soma(a = 0, b = 0, c = 0):

    s = a + b + c
    return s
resultado = soma(1,2,3)
resultado2 = soma(75,45,52)

print(f"a primeira soma vale {resultado} e a segunda vale {resultado2}")


