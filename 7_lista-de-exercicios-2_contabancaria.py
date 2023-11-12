# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.

# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela 
#    fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.

# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança", "propriedades", "encapsulamento" e "classe abstrata".



from abc import ABC, abstractmethod

class cliente():
    def __init__(self, nome, telefone, renda_mensal):
        self._primeiro_nome = nome.split(" ")[0].title()
        self._ultimo_nome = nome.split(" ")[-1]
        self._telefone = telefone
        self._renda_mensal = renda_mensal

    @property
    def nome(self):
        return self._primeiro_nome + " " + self._ultimo_nome

    @nome.setter
    def nome(self, novo_primeiro_nome, novo_ultimo_nome):
        if not isinstance(novo_primeiro_nome, str) or not isinstance(novo_ultimo_nome, str):
            raise TypeError("Tipo de variável deve ser str")
        self._primeiro_nome = novo_primeiro_nome
        self._ultimo_nome = novo_ultimo_nome

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, novo_tel):
        if not isinstance(novo_tel, str):
            raise TypeError("Tipo de variável deve ser str")
        self._telefone = novo_tel

    @property
    def renda_mensal(self):
        return self.__renda_mensal

    @abstractmethod
    def tem_cheque_especial(self):
        pass


class clientemulher(cliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)

    def tem_cheque_especial(self):
        return True


class clientehomem(cliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)

    def tem_cheque_especial(self):
        return False


class ContaCorrente:
    def __init__(self, titular):
        self.__saldo = 0.0
        self.__operacoes = []
        self.__titulares = []
        self.adicionar_titular(titular)

    def adicionar_titular(self, titular):
        self.__titulares.append(titular.nome)

    def depositar(self, valor: float):
        self.__saldo += valor
        self.__operacoes.append(f"Depósito de R${valor:.2f}")

    def sacar(self, valor: float):
        titular = self.__titulares[0]
        if titular.tem_cheque_especial():
            if valor <= self.__saldo or (self.__saldo - valor) <= titular.renda_mensal:
                self.__saldo -= valor
                self.__operacoes.append(f"Saque de R$ {valor:.2f}")
            else:
                raise ValueError("Saldo insuficiente")
        else:
            if valor <= self.__saldo:
                self.__saldo -= valor
                self.__operacoes.append(f"Saque de R${valor:.2f}")
            else:
                raise ValueError("Saldo insuficiente")

    @property
    def saldo(self):
        return self.__saldo

    @property
    def operacoes(self):
        return self.__operacoes


cliente_mulher = clientemulher("Maria Macedo", "747474", 30000.0)
cliente_homem = clientehomem("Julio", "9798987897", 1000.0)

conta1 = ContaCorrente(cliente_mulher)
conta2 = ContaCorrente(cliente_homem)

print(conta1.saldo)
print(conta2.saldo)
print()

conta1.depositar(5000.0)
conta2.depositar(50.0)

print(conta1.saldo)
print(conta2.saldo)
print()

print(conta1.operacoes)
print(conta2.operacoes)
print()
