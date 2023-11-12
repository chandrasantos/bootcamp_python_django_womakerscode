import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()


# Crie uma tabela chamada "alunos" com os seguintes campos: id(inteiro), nome (texto), idade (inteiro) e curso (texto).
#result= cursor.execute('''create table alunos(id INTERGER, nome VARCHAR(250), idade INTERGER, curso VARCHAR(250))''')

# Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior
#result= cursor.execute('''insert into alunos(id, nome, idade, curso) values 1, "Camila", 20, "Dados"), (2, "Maria", 22, "Dados"), (3, "Joana", 24, "Engenharia"), (4, "Clara", 25, "Dados"), (5, "Simone", 30, "Engeharia")''')

#Consultas Básicas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".
#result = cursor.execute('''select * from alunos''')

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
# result = cursor.execute('''select nome, idade from alunos where idade > 20''')

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
# result = cursor.execute('''select * from alunos where curso = "Engenharia" order by nome''')

#d) Contar o número total de alunos na tabela
# result = cursor.execute('''select count(*) from alunos''')

#4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.
#result = cursor.execute('''update alunos set idade = 28 where id = 1''')

#b) Remova um aluno pelo seu ID.
#result = cursor.execute('''delete from alunos where id = 1''')

#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.
#result = cursor.execute('''create table clientes (id INTEGER primary key, nome VARCHAR(250), idade INTEGER, saldo FLOAT)''')
#result = cursor.execute('''insert into clientes (id, nome, idade, saldo) values (1, "Camila", 20, 1000), (2, "Maria", 33, 200), (3, "Joana", 24, 500), (4, "Clara", 40, 1200), (5, "Simone", 30, 300)''')

#6. Consulta e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
#result = cursor.execute('''select nome, idade from clientes where idade >=30''')

#b) Calcule o saldo médio dos clientes.
#result = cursor.execute('''select AVG(saldo) from clientes''')

#c) Encontre o cliente com o saldo máximo.
#result = cursor.execute('''select nome from clientes where saldo = (select max(saldo) from clientes)''')

#d) Conte quantos clientes têm saldo acima de 1000.
#result = cursor.execute('''select count(*) from clientes where saldo >=1000''')

#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.
#result = cursor.execute('''update clientes set saldo = 2000 where id =1''')

#b) Remova um cliente pelo seu ID.
#result = cursor.execute('''delete from clientes where id = 1''')

#8. Junção de Tabelas
#Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). 
#result = cursor.execute('''create table compras (id INTEGER primary key, cliente_id INTEGER, produto VARCHAR(250), valor FLOAT, CONSTRAINT fk_clientes FOREIGN KEY (cliente_id) REFERENCES clientes (id))''')
#result = cursor.execute('''insert into compras (id, cliente_id, produto, valor) values (1,1, 'caderno', 20.0), (2,1,"caneta", 1.10), (3, 2, "caderno", 2.0)''')

# Insira algumas compras associadas a clientes existentes na tabela "clientes". Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
result = cursor.execute('''select c.nome, co.produto, co.valor from compras as co inner join clientes as c on c.id = co.cliente_id''')
for item in result:
    print(item)


# as informações só são enviadas quando chegar nesse comando
conexao.commit()

# encerra o processo
conexao.close 
