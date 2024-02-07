aluno = {
    "Nome": input("Digite o nome do aluno: "),
    "Nota1": float(input("Digite a primeira nota do aluno: ")),
    "Nota2": float(input("Digite a segunda nota do aluno: ")),
    "Nota3": float(input("Digite a terceira nota do aluno: "))
}

# Calcula a média
media = (aluno["Nota1"] + aluno["Nota2"] + aluno["Nota3"]) / 3

# Determina a situação
if media >= 9.5:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

# Adiciona a média e a situação ao dicionário
aluno["Média"] = media
aluno["Situação"] = situacao

# Exibe todo o conteúdo do dicionário

print("\nDados do aluno:")
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
