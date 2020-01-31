import pymysql # para o MySQL
from time import sleep


def teste_banco():
    
    import Limpeza
    Limpeza.limpar()
    
    print('-=-'*10)
    print('TESTANDO BANCO DE DADOS')
    print('-=-'*10)

    #COLETANDO INFORMAÇÕES DE CONEXÃO DO BANCO
    host = str(input('Digite o ip:'))         
    user = str(input('Digite o usuário:'))         
    password = str(input('Digite a password:'))   
    port = int(input('Digite a porta:'))
    db = str(input('Informe o banco:'))
    print('-=-'*10)

    sleep(2)
    print('INICIANDO CONEXÃO...')
    sleep(2)
    print('CONECTANDO NO BANCO...\n')
    sleep(2)
    
    #TESTE DE CONEXÃO COM BANCO 
    try:
        db = pymysql.connect(host, user, password, db, port)
        print('-=-'*10)
        print('CONEXÃO COM O BANCO - OK')
        print('-=-'*10)
        db.close()
        import Menu
        Menu.MenuPrincipal()


    except:
        print('-=-'*10)
        print('CONEXÃO COM O BANCO - FALHA')
        print('-=-'*10)
        db.close()
        import Menu
        Menu.MenuPrincipal()
        