"""
Avaliação – Python +    SQLite
Tema: CRUD em 'alunos'

O que o script deve fazer:
1) Criar 'escola.db'
2) Criar tabela 'alunos' -> Seguindo o diagrama
3) Inserir registros na tabela alunos
4) Listar todos
5) Buscar por id
6) Atualizar registros
7) Deletar registros

"""

import sqlite3
# Passo 1 - Conectar/criar o banco de dados
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Passo 2 - Criar tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    email TEXT
             )
''')

print('Tabela criada com sucesso!\n')

# Passo 3 - Inserir dados
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('Sophia', 18, 'sophia@gmail.com'))
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('Yan', 17, 'yan@gmail.com'))
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('Rafaela', 17, 'rafaela@gmail.com'))
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('Ana', 18, 'ana@gmail.com'))
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('Lucas', 17, 'lucas@gmail.com'))
conn.commit()

print("Dados inseridos!\n")

# Passo 4 - Listar todos
print("Lista de alunos cadastrados:")
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

# Passo 5 - Atualizar um registro
cursor.execute('UPDATE alunos SET email = ? WHERE nome = ?',
               ('sophia.dev@gmail.com', 'Sophia'))
conn.commit()

print('Após atualização do email da Sophia:')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

# Passo 6 - Deletar um registro
cursor.execute('DELETE FROM alunos WHERE nome = ?', ('Rafaela',))
conn.commit()

print('Após deletar do email da Rafaela:')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

# Encerrar conexão
conn.close()
