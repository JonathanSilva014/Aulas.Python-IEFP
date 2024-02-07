"""
aluno = {"Nome": "Cesar", "Média": 14}
print(f"O Aluno {aluno['Nome']} tem a média de {aluno['Média']} valores.")

if aluno["Média"] >= 9.5:
    aluno["Situação"] = "Aprovado"
else:
    aluno ["Situação"] = "Reprovado"
"""

"""
aluno = dict()

aluno["Nome"] = input("Digite o nome do aluno: ")
aluno["Ex1"] = int(input("Digite a nota do 1º exame: "))
aluno["Ex2"] = int(input("Digite a nota do 2º exame: "))
aluno["Ex3"] = int(input("Digite a nota do 3º exame: "))

print(aluno.items())

aluno["Média"] = (aluno["Ex1"] + aluno["Ex2"] + aluno["Ex3"]) / 3

print(f"A média do aluno {aluno['Nome']} é {aluno['Média']}")
"""

cidade = {"Nome": "Porto", "Código": "OPO", "Baixa": "Ribeira", "Rio": "Douro"}
cidade2 = {"Nome": "Viseu", "Código": "LX", "Baixa": "Chiado", "Rio": "Tejo"}

pais = list()
pais.append(cidade)
pais.append(cidade2)

print(pais)

for c in range(0, len(pais)):  # Correção: Adição de dois pontos (:)
    print(f"Cidade: {pais[c]['Nome']}")

"""
for k, v in cidade.items()
    print(f"O {k} é {v}")
"""