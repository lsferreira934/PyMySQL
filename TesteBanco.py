import pymysql # para o MySQL
from time import sleep
import Layout

def teste_banco():
    
    import Limpeza
    Limpeza.limpar()
    
    Layout.linha()
    print('TESTANDO BANCO DE DADOS')
    Layout.linha()

    #COLETANDO INFORMAÇÕES DE CONEXÃO DO BANCO
    host = str(input('Digite o ip:'))         
    user = str(input('Digite o usuário:'))         
    password = str(input('Digite a password:'))   
    port = int(input('Digite a porta:'))
    db = str(input('Informe o banco:'))
    Layout.linha()

    sleep(2)
    print('INICIANDO CONEXÃO...')
    sleep(2)
    print('CONECTANDO NO BANCO...\n')
    sleep(2)
    
    #TESTE DE CONEXÃO COM BANCO 
    try:
        db = pymysql.connect(host, user, password, db, port)
        Layout.linha()
        print('CONEXÃO COM O BANCO - OK')
        Layout.linha()
        db.close()
        import Menu
        Menu.MenuPrincipal()


    except:
        Layout.linha()
        print('CONEXÃO COM O BANCO - FALHA')
        Layout.linha()
        import Menu
        Menu.MenuPrincipal()
        