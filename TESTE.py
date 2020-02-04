import pymysql # para o MySQL

#CONFIGURAÇÕES PARA ACESSO DO BANCO
host = '127.0.0.1'
user = 'root'
password = ''
port = 3306
banco = 'cadastro'



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










