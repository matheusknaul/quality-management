import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('instance/mydatabase.db')

# Criar um cursor
cursor = conn.cursor()

# Listar tabelas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

# Verificar a estrutura da tabela 'supplier'
cursor.execute("PRAGMA table_info(supplier);")
columns = cursor.fetchall()
print("Supplier Table Columns:", columns)

# Consultar dados da tabela 'supplier'
cursor.execute("SELECT * FROM supplier;")
rows = cursor.fetchall()
print("Supplier Table Data:", rows)

# Fechar a conexão
conn.close()
