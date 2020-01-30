import pymysql # para o MySQL
from time import sleep

def criar_banco():

    print('-=-'*10)
    print('CRIADOR DE BANCO DE DADOS')
    print('-=-'*10)

    #CONFIGURAÇÕES PARA ACESSO DO BANCO

    host = str(input('Digite o ip:'))         
    user = str(input('Digite o usuário:'))         
    senha = str(input('Digite a password:'))   
    
    print('-=-'*10)

    db = pymysql.connect(host, user, senha)
    cursor = db.cursor()

    print('[1] LISTAR BANCOS\n'
          '[2] CRIAR BANCOS\n'                 
          '[3] DELETAR BANCOS\n'
          '[4] VOLTAR\n')
    opc = int(input('-->'))

    if opc == 1:
        print('-=-'*10)
        print('LISTAR BANCOS')
        print('-=-'*10)
        modb = 'SHOW DATABASES'
        cursor.execute(modb)
        for x in cursor:
            print(x)
        criar_banco()
    elif opc == 2:
        print('-=-'*10)
        print('CRIAR BANCOS')
        print('-=-'*10)
        nomedb = str(input('Digite o nome do seu Banco:'))
        criardb = (f'CREATE DATABASE{nomedb}')
        cursor.execute(criardb)
        criar_banco()
    elif opc == 3:
        print('-=-'*10)
        print('DELETAR BANCOS')
        print('-=-'*10)
        nomedb = str(input('Digite o Banco:'))
        dedb = (f'DROP DATABASE {nomedb}')
        cursor.execute(dedb)
        criar_banco()
    elif opc == 4:
        import Menu
        Menu.MenuPrincipal()


