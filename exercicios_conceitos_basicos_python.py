# Exercícios: Conceitos Básicos em Python

'''
1. Faça um Programa que peça um número e então mostre a
mensagem: -> O número informado foi [número].

numero = input("Digite um número: ")
print("O número informado foi", numero)
'''

''' 2. Faça um Programa que peça dois números e imprima a soma.
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
soma = numero1 + numero2
print("A soma dos números é:", soma) '''


''' 3. Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Fahrenheit. 

temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
print("A temperatura em graus Fahrenheit é:", temperatura_fahrenheit) '''

''' 4. Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês. Calcule e mostre o total do
seu salário no referido mês. '''

valor_por_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario_mensal = valor_por_hora * horas_trabalhadas
print("O total do seu salário no referido mês é:", salario_mensal)
