import pymysql # para o MySQL
from time import sleep


def teste_banco():

    print('-=-'*10)
    print('TESTANDO BANCO DE DADOS')
    print('-=-'*10)

    #CONFIGURAÇÕES PARA ACESSO DO BANCO

    host = str(input('Digite o ip:'))         
    user = str(input('Digite o usuário:'))         
    senha = str(input('Digite a password:'))   
    porta = int(input('Digite a porta:'))
    banco = str(input('Informe o banco:'))
    print('-=-'*10)

    

    sleep(2)
    print('INICIANDO CONEXÃO...')
    sleep(2)
    print('CONECTANDO NO BANCO...\n')
    sleep(2)
    
    #TESTE DE CONEXÃO COM BANCO 
    
    try:
        db = pymysql.connect(host, user, senha, porta, banco)
        print('-=-'*10)
        print('CONEXÃO COM O BANCO - OK')
        print('-=-'*10)
        db.close()
        import Menu
        Menu.MenuPrincipal()


    except:
        print('-=-'*10)
        print('CONEXÃO COM O BANCO - OFFLINE')
        print('-=-'*10)
        db.close()
        import Menu
        Menu.MenuPrincipal()