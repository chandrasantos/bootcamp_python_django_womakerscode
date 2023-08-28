'''1. Crie um programa que leia quanto dinheiro uma pessoa tem na carteira, e calcule quanto poderia comprar de cada moeda estrangeira. Considere a tabela de conversão abaixo: Dólar Americano: R$ 4,91, Peso Argentino: R$ 0,02, Dólar Australiano: R$ 3,18, Dólar Canadense: R$ 3,64, Franco Suiço: R$ 0,42, Euro: R$ 5,36, Libra esterlina: R$ 6,21

def main():
    dinheiro_na_carteira = float(input("Digite quanto dinheiro você tem (R$): "))
    
    conversoes = {
        "Dólar Americano": 4.91,
        "Peso Argentino": 0.02,
        "Dólar Australiano": 3.18,
        "Dólar Canadense": 3.64,
        "Franco Suiço": 0.42,
        "Euro": 5.36,
        "Libra esterlina": 6.21
    }
    
    print("\nQuantidade de moeda estrangeira que você poderia comprar:")
    for moeda, taxa in conversoes.items():
        quantidade = dinheiro_na_carteira / taxa
        print(f"{moeda}: {quantidade:.2f}")
    
if __name__ == "__main__":
    main()



2. Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 80,00 por dia e R$ 0,20 por km rodado.

km_percorridos = float(input("Digite a quantidade de km percorridos: "))
dias_alugados = int(input("Digite a quantidade de dias alugados: "))

preco_por_dia = 80.00
preco_por_km = 0.20

preco_total = (preco_por_dia * dias_alugados) + (preco_por_km * km_percorridos)
print(f"O preço a pagar é: R$ {preco_total:.2f}")


3. Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário. Se o salário for até R$ 1000,00 o funcionário terá 20% de aumento. Entre R$ 1001,00 até R$ 2800,00 o funcionário terá 10% de aumento. Acima de R$ 2801,00 o funcionário terá 5% de aumento.


salario_atual = float(input("Digite o salário atual: "))

if salario_atual <= 1000.00:
    novo_salario = salario_atual * 1.20  # Aumento de 20%
elif salario_atual <= 2800.00:
    novo_salario = salario_atual * 1.10  # Aumento de 10%
else:
    novo_salario = salario_atual * 1.05  # Aumento de 5%
print(f"O novo salário é: R$ {novo_salario:.2f}")


4. Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor númerico. Ex: n = leiaInt(‘Digite um n’)                                                                                                                                                                                                   
'''
def leiaInt(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Digite um número inteiro válido.")

# Exemplo de uso
n = leiaInt('Digite um número inteiro: ')
print(f'O número digitado é: {n}')
