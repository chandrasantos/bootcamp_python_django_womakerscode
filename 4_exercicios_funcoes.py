''' 1. Faça um programa, com uma função que necessite de três
argumentos, e que forneça a soma desses três argumentos. 

def soma_tres_numeros(a, b, c):
    soma = a + b + c
    return soma

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

resultado = soma_tres_numeros(num1, num2, num3)
print("A soma dos três números é:", resultado) 

2. "Reverso do número. Faça uma função que retorne o reverso de
um número inteiro informado. Por exemplo: 127 -> 721.

def reverso_numero(numero):
    numero_str = str(numero)
    reverso_str = numero_str[::-1]
    reverso = int(reverso_str)
    return reverso

numero = int(input("Digite um número inteiro: "))
reverso = reverso_numero(numero)
print("O reverso do número é:", reverso)



3. Escreva um script que pergunta ao usuário se ele deseja
converter uma temperatura de grau Celsius para Fahrenheit ou
vice-versa. Para cada opção, crie uma função. Crie uma terceira,
que é um menu para o usuário escolher a opção desejada, onde
esse menu chama a função de conversão correta. '''

def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def menu():
    print("Escolha a o tipo de temperatura:")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    escolha = int(input("Digite o número da opção desejada: "))

    if escolha == 1:
        celsius = float(input("Digite a temperatura em Celsius: "))
        resultado = celsius_para_fahrenheit(celsius)
        print(f"{celsius}°C é igual a {resultado:.2f}°F")
    elif escolha == 2:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        resultado = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit}°F é igual a {resultado:.2f}°C")
    else:
        print("Opção inválida")

menu()
