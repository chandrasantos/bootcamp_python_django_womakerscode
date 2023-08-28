'''1."Faça um Programa que peça as quatro notas de 10 alunos,
calcule e armazene numa lista a média de cada aluno, imprima o
número de alunos com média maior ou igual a 7.0.

medias_alunos = []
for i in range(10): 
    notas = []  
    for j in range(4):  
        nota = float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    medias_alunos.append(media)
alunos_aprovados = sum(1 for media in medias_alunos if media >= 7.0)
print(f"Número de alunos com média maior ou igual a 7.0: {alunos_aprovados}")


2. Programa nome ao contrário em maiúsculas. Faça um programa
que permita ao usuário digitar o seu nome e em seguida mostre o
nome do usuário de trás para frente utilizando somente letras
maiúsculas. Dica: lembre−se que ao informar o nome o usuário
pode digitar letras maiúsculas ou minúsculas.

nome = input("Digite o seu nome, em maiscúlas ou minúsculas: ")
nome_invertido = nome.upper()[::-1]
print(nome_invertido)


3. Escreva um programa em Python que onde todos os valores em
um dicionário são emitidos. Se sim , imprima True. Caso contrário,
imprima Falso.

def verifica_valores(animais):
    for valor in animais.values():
        if valor is None or valor == "":
            return False
    return True
exemplo_animais = {
    "anfibios": "sapo",
    "aves": "calopsita",
    "mamiferos": "gato",
    "repteis": ""
}
resultado = verifica_valores(exemplo_animais)
if resultado:
    print("True")
else:
    print("False")

def verifica_valores(animais):
    for valor in animais.values():
        if valor is None or valor == "":
            return False
    return True
exemplo_animais = {
    "anfibios": "sapo",
    "aves": "calopsita",
    "mamiferos": "gato",
    "repteis": "cobra"
}
resultado = verifica_valores(exemplo_animais)
if resultado:
    print("True")
else:
    print("False")

4. "Utilizando listas faça um programa que faça 5 perguntas para
uma pessoa sobre um crime. As perguntas são:
""Telefonou para a vítima?""
""Esteve no local do crime?""
""Mora perto da vítima?""
""Devia para a vítima?""
"Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime. Se a pessoa responder positivamente a 2 questões
ela deve ser classificada como ""Suspeita"", entre 3 e 4 como
""Cúmplice"" e 5 como ""Assassino"". Caso contrário, ele será
classificado como ""Inocente"".
'''

def fazer_pergunta(pergunta):
    resposta = input(pergunta).strip().lower()  
    return resposta == "sim" or resposta == "s"  

perguntas = [
    "Telefonou para a vítima? ",
    "Esteve no local do crime? ",
    "Mora perto da vítima? ",
    "Devia para a vítima? ",
    "Já trabalhou com a vítima? "
]

respostas_positivas = 0

for pergunta in perguntas:
    if fazer_pergunta(pergunta):
        respostas_positivas += 1
if respostas_positivas == 2:
    classificacao = "Suspeita"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"
print(f"Classificação: {classificacao}")
