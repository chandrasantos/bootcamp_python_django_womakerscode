# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
class Carro:
    def __init__(self, cor, modelo):
        self.ligado = False  # Define o atributo "ligado" como False por padrão.
        self.cor = cor  # Define o atributo "cor" com o valor passado como argumento.
        self.modelo = modelo  # Define o atributo "modelo" com o valor passado como argumento.
        self.velocidade = 0  # Define o atributo "velocidade" como 0 por padrão.

    def liga(self):
        if not self.ligado:  # Verifica se o carro já está ligado.
            self.ligado = True  # Define o atributo "ligado" como True.
            print("O carro está ligado.")
        else:
            print("O carro já está ligado.")

    def desliga(self):
        if self.ligado:  # Verifica se o carro já está desligado.
            self.ligado = False  # Define o atributo "ligado" como False.
            print("O carro está desligado.")
        else:
            print("O carro já está desligado.")

    def acelera(self, velocidade):
        if self.ligado:  # Verifica se o carro está ligado.
            self.velocidade += velocidade  # Aumenta a velocidade do carro.
            print(f"O carro acelerou para {self.velocidade} km/h.")
        else:
            print("O carro precisa estar ligado para acelerar.")

    def desacelera(self, velocidade):
        if self.ligado:  # Verifica se o carro está ligado.
            if velocidade <= self.velocidade:  # Verifica se a velocidade informada é menor ou igual à atual.
                self.velocidade -= velocidade  # Diminui a velocidade do carro.
                print(f"O carro desacelerou para {self.velocidade} km/h.")
            else:
                print("A velocidade informada é maior do que a atual.")
        else:
            print("O carro precisa estar ligado para desacelerar.")

# Crie uma instância da classe carro.
# Cria uma instância da classe Carro com cor vermelha e modelo Fiat.
carro1 = Carro("vermelho", "Fiat")

# Faça o carro "andar" utilizando os métodos da sua classe.
# Liga o carro e acelera até 50 km/h.
carro1.liga()
carro1.acelera(50)

# Faça o carro "parar" utilizando os métodos da sua classe.
# Desacelera até 30 km/h e desliga o carro.
carro1.desacelera(20)
carro1.desliga()

