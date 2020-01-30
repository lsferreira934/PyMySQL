import pymysql # para o MySQL

#CONFIGURAÇÕES PARA ACESSO DO BANCO
host = '127.0.0.1'
user = 'root'
password = ''
port = 3306
db = 'cadastro'



#TESTE DE CONEXÃO COM BANCO 

try:
    db = pymysql.connect(host, user, password, db, port)
    print('CONEXÃO COM O BANCO - OK')

except:
        print('CONEXÃO COM O BANCO - OFFLINE')


#LOCAÇÃO DE MEMORIA(CARREGAMENTO DO CODÍGO DO BANCO) "QWERY"
cursor = db.cursor()

nome_banco = 'cadastro'
nome_tabela = 'LISTA'

dedb = (f'DROP DATABASE {nome_banco}')
detb = (F'DROP TABLE {nome_tabela}')

db = (f'CREATE DATABASE{nome_banco}')
tb = (f'CREATE TABLE{nome_tabela}')

modb = 'SHOW DATABASES'
motb = 'SHOW TABLES'

cursor.execute(modb)

def todosdbs():
    for x in cursor:
        print(x)

def todastbs():
    for x in cursor:
        print(x)


db.closse()










