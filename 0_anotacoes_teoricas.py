print ('Hello Word')

# comentário de 1 linha

'''
comentario 
de 3 
linhas
'''

''' variaveis sao nomes dados a valores, funcoes, acoes
int, inteiro, 1,5, 10
float, decimal, 1.5, 
string, texto, python
boolean , logico, sim/não

operacoes matematicas
sema +
subtracao -
multiplicacao *
divisao /
divisao inteira // 
incremento +=
decremento -=
resto 10%3 o resto da divisao é 1

ordem de precedencia - oq vem antes e depois, usa parenteses ()
multiplica e divisao vem antes de soma e divisao, padrao.

operadores relacionais
==
>
>=
<=
<
!=


formtacao
coloca texto e numero no resultado
# print(f'a soma é {numero}')

str.format mostrar qts casas decimais tera o nosso codigo. 
print(f'{valor:.2f}')

numero = "1" + 2
print(numero)

IF - SE \ ELSE SENAO serve para verificar algo é verdeiro ou falso 
while enquanto ele fica rodando enquanto uma informacao for verdeira
for loopings infinitos ele executa para cada informacao que for verdadeira. percorrer listas


listas = [] armazena nomes em bancos de dados
exemplo: 
lançar a mao
lista_frutas = [] 
lista_frutas.append('maça')

fruta= input('Digite sua fruta:')
lista_frutas.append(fruta)
Aqui a pessoa pode preencher o que ela quer.

usa o append para incluir itens na lista 


tupla = ('maça', 'uva)
valores nao podem ser alterados
tuplas nao sao muito usadas 

dicionários = {}
ele parece um dicionario do mundo real. um valor associado a um conjunto.
dicionario = {}
dicionario['Maça'] = 'é uma fruta'
dicionario['gato'] = 'é um animal'

funcoes
sao instrucoes relacionadas q executam tarefas. 
declaracao
instrucoes ficam dentro da funcao assim
defmostrar_mensagem():
chamar a funcao
mostrar_mensagem()

parametros = passagem de valores para diferentes funções


manipulacao de arquivos
file = arquivo.txt

variavel que recebe o arquivo

abertura
arquivo_leitura = open(file, "r") somente para leitura

abertura para escrita
arquivo_escrita = open(file, "w")

abertura de arquivos binarios
arquivo_binario = open(file, "wb")

escrita
arquivo_escrita = open(file, "w")
arquivo_escrita.write("Texto a ser escrito")
arquivo_escrita.close()

leitura
arquivo_leitura = open(file, "r")
leitura = arquivo_escrita.read()
print(leitura)
arquivo_leitura.close()


tratamento de excecoes
try e except servem para tratar erros 

try - tente
except - excessao

ex: divisao por zero
divisao por string

'''