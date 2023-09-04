def maiorNota(disciplinas):
    maiorNotaNoMomento = None
    disciplinaComMaiorNota = None

    for nome, disciplina in disciplinas.items():
        if maiorNotaNoMomento is None or disciplina["nota"] > maiorNotaNoMomento:
            disciplinaComMaiorNota = nome
            maiorNotaNoMomento = disciplina["nota"]

    return f'Maior: {disciplinaComMaiorNota}, {maiorNotaNoMomento}'
   
def menorNota(disciplinas):
    menorNotaNoMomento = None
    disciplinaComMenorNota = None

    for nome, disciplina in disciplinas.items():
        if menorNotaNoMomento is None or disciplina["nota"] < menorNotaNoMomento:
            disciplinaComMenorNota = nome
            menorNotaNoMomento = disciplina["nota"]

    return f'Menor: {disciplinaComMenorNota}, {menorNotaNoMomento}'
   
def mediaPonderada(disciplinas):
    soma = 0
    somaDosPesos = 0

    for disciplina in disciplinas.values():
        soma += disciplina["nota"] * disciplina["peso"]
        somaDosPesos += disciplina["peso"]
        media = soma / somaDosPesos
        
    return f'Média: {media}'

quantidadeDeDisciplinas = int(input("Quantas disciplinas você quer adicionar?"))

listaDisciplinas = {}

while quantidadeDeDisciplinas > 0:
    nome = input("Qual é o nome da matéria?")
    nota = int(input("Qual é a nota da matéria?"))
    peso = int(input("Qual é o peso da matéria?"))

    disciplina = {
        "nota": nota,
        "peso": peso
    }

    listaDisciplinas[nome] = disciplina
    quantidadeDeDisciplinas -= 1

print(maiorNota(listaDisciplinas))
print(menorNota(listaDisciplinas))
print(mediaPonderada(listaDisciplinas))