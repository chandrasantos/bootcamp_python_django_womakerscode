# observação: esse arquivo tem que estar na mesma pasta que o banco de dados sqllite
# essa é a estrutura de um banco de dados
#baixa o banco, conecta com o banco criado

import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

# executa os comandos
#try:
#    cursor.execute('CREATE, TABLE usuarios(id INT, nome VARCHAR(100), endereço VARCHAR(100), email VARCHAR(100));')
#except sqlite3.OperationalError:
#    pass

#    cursor.execute('CREATE, TABLE gerentes(id INT, nome VARCHAR(100), endereço VARCHAR(100), email VARCHAR(100));')

#cursor.execute('ALTER TABLE usuario RENAME TO users')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')

#cursor.execute('DROP TABLE produtos')
#cursor.execute('INSERT INTO usuario(id, nome, endereço, email, telefone) VALUES(1,"Isadora", "França", "isa@gmail.com", 123456)')
#cursor.execute('INSERT INTO gerentes(id, nome, endereço, email, telefone) VALUES(9,"Bia", "Brasil", "bea@gmail.com", 987456321)')
#cursor.execute('DELETE FROM usuario where id=1')
# dados = cursor.execute('SELECT * FROM usuario ORDER BY nome DESC')
# for usuario in dados:
#    print(usuario)

#cursor.execute('UPDATE usuario SET endereco="Minas Gerais" WHERE nome="Jose"')

# dados = cursor.execute('SELECT DISTINCT * FROM usuario LIMIT 3')
# for usuario in dados:
#    print(usuario)

# dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome')
# for usuario in dados:
#    print(usuario)

# dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id>3')
# for usuario in dados:
#    print(usuario)

# dados = cursor.execute('SELECT FROM usuario INNER JOIN gerentes ON usuario.id=gerentes.id')
# for usuario in dados:
#    print(usuario)

# as informações só são enviadas quando chegar nesse comando
conexao.commit()

# encerra o processo
conexao.close 

