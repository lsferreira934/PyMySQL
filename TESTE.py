import pymysql # para o MySQL

#CONFIGURAÇÕES PARA ACESSO DO BANCO
host = '127.0.0.1'
user = 'root'
password = ''
port = 3306
db = 'cadastro'

db = pymysql.connect(host, user, password, port, db)
cursor = db.cursor()

print('LISTAR TABELAS')
            
motb = 'SHOW TABLES'
cursor.execute(motb)
print('|TODAS AS TABELAS     |')
print('-' * 22)
#for x in cursor:
#    x = list(x) #CONVERTENDO TULIPAS EM LISTA
#    x = str(x).strip('[]') #CONVERTENDO LISTA EM STRINGS E REMOVENDO OS COLCHETES 
#    print(f'|{x.rstrip().rjust(4).ljust(20).upper()}|') #PRINT FORMATADO DOS BANCOS



'''
#TESTE DE CONEXÃO COM BANCO 

try:
    db = pymysql.connect(host, user, password, banco, port)
    print('CONEXÃO COM O BANCO - OK')
    
    #LOCAÇÃO DE MEMORIA(CARREGAMENTO DO CODÍGO DO BANCO) "QWERY"
    cursor = db.cursor()

    #SELEÇÃO DO BANCO E DA TABELA
    nome_banco = 'cadastro'
    nome_tabela = ''

    #SELEIONAR O BANCO
    sedb = (f'USE {nome_banco}')
    setb = (f'USE {nome_tabela}')

    #CRIAÇÃO 
    crdb = (f'CREATE DATABASE {nome_banco}')
    crtb = (f'CREATE TABLE {nome_tabela}')

    #PAGAR
    dedb = (f'DROP DATABASE {nome_banco}')
    detb = (F'DROP TABLE {nome_tabela}')

    #MOSTRAR
    modb = 'SHOW DATABASES'
    motb = 'SHOW TABLE'

    cursor.execute(modb)

    def todosdbs():
        for x in cursor:
            print(x)

    def todastbs():
        for x in cursor:
            print(x)
    #db.closse()

except:
    print('CONEXÃO COM O BANCO - OFFLINE')
    #db.closse()
'''









