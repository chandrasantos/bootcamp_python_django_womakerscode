''' 1. Faça um Programa que peça dois números e imprima o maior
deles. 

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
if numero1 > numero2:
    print("O maior número é:", numero1)
elif numero2 > numero1:
    print("O maior número é:", numero2)
else:
    print("Os números são iguais.") 

2. Faça um Programa que pergunte em que turno você estuda. Peça
para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor
Inválido!", conforme o caso.

turno = input("Em qual turno você estuda? Digite, em minúsculas, m-matutino, v-vespertino ou n-noturno: ")
if turno == "m":
    print("Bom Dia!")
elif turno == "v":
    print("Boa Tarde!")
elif turno == "n":
    print("Boa Noite!")
else:
    print("Valor Inválido!")

3. Faça um programa que peça uma nota, entre zero e dez. Mostre
uma mensagem caso o valor seja inválido e continue pedindo até
que o usuário informe um valor válido.

while True:
    try:
        nota = float(input("Digite uma nota entre zero e dez: "))        
        if 0 <= nota <= 10:
            break 
        else:
            print("Valor inválido. Digite novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número válido.")
print("Você inseriu uma nota válida:", nota)'''

nota = int(input("Digite uma nota entre zero e dez: "))
while 0 > nota or nota > 10:
    print("Valor inválido. A nota deve estar entre zero e dez.")
    nota = int(input("Digite uma nota entre zero e dez: "))
print("Você inseriu uma nota válida:", nota)
 