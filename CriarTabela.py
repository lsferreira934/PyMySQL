import pymysql # para o MySQL
from time import sleep

# MANIPULAÇÃO DE TABELAS
def criar_tabela():
    
    #FUNÇÃO DE LIMPEZA DA TELA
    import Limpeza
    Limpeza.limpar()
    
    print('-=-'*10)
    print('CRIADOR DE TABELA')
    print('-=-'*10)

    
    #COLETANDO INFORMAÇÕES DE CONEXÃO DO BANCO
    host = str(input('Digite o ip:'))         
    user = str(input('Digite o usuário:'))         
    password = str(input('Digite a password:'))   
    print('-=-'*10)

    sleep(2)
    print('INICIANDO CONEXÃO...')
    sleep(2)
    print('CONECTANDO AO BANCO...\n')
    sleep(2)

    #TESTE DE CONEXÃO COM BANCO     
    try:    
        db = pymysql.connect(host, user, password)
        cursor = db.cursor()  
        print('-=-'*10)
        print('CONEXÃO COM O BANCO - OK')
        print('-=-'*10)
        sleep(1)

        #FUNÇÃO DE LIMPEZA DA TELA
        import Limpeza
        Limpeza.limpar()
        print('[1] LISTAR TABELA\n'
              '[2] CRIAR TABELA\n'                 
              '[3] DELETAR TABELA\n'
              '[4] VOLTAR\n')
        opc = int(input('-->'))
        
        if opc == 1:
            
            #FUNÇÃO DE LIMPEZA DA TELA
            import Limpeza
            Limpeza.limpar()

            print('-=-'*10)
            print('LISTAR TABELAS')
            print('-=-'*10)
            modb = 'SHOW TABLES'
            cursor.execute(modb)
            for x in cursor:
                print(x)
            db.close()
            criar_banco()

        elif opc == 2:

            #FUNÇÃO DE LIMPEZA DA TELA
            import Limpeza
            Limpeza.limpar()
            
            print('-=-'*10)
            print('CRIAR BANCOS')
            print('-=-'*10)
            nomedb = str(input('Digite o nome do seu Banco:'))
            criardb = (f'CREATE DATABASE {nomedb}\n')
            
            sleep(1)
            print('CONECTANDO AO BANCO...')
            sleep(1)
            print(f'CRIANDO NOVO BANCO DE DADOS: {nomedb}...')
            sleep(1)
            print(f'BANCO DE DADOS {nomedb} CRIADO COM SUCESSO!\n')
            sleep(2)
            print('-=-'*10)
            cursor.execute(criardb)
            db.close()
            criar_banco()

        elif opc == 3:
            
            #FUNÇÃO DE LIMPEZA DA TELA
            import Limpeza
            Limpeza.limpar()
            
            print('-=-'*10)
            print('DELETAR BANCOS')
            print('-=-'*10)
            nomedb = str(input('Digite o Banco:'))
            dedb = (f'DROP DATABASE {nomedb}\n')
            
            sleep(1)
            print('CONECTANDO AO BANCO...')
            sleep(1)
            print(f'EXCLUINDO BANCO DE DADOS: {nomedb}...')
            sleep(1)
            print(f'BANCO DE DADOS {nomedb} EXCUIDO COM SUCESSO!\n')
            sleep(2)
            print('-=-'*10)
            cursor.execute(dedb)
            db.close()
            criar_banco()

        elif opc == 4:
            
            #FUNÇÃO DE LIMPEZA DA TELA
            import Limpeza
            Limpeza.limpar()
            
            print('VONTANDO PARA O MENU PINCIPAL')
            sleep(1)
            db.close()
            import Menu
            Menu.MenuPrincipal()

    #QUANDO FALHAR O TEXTE DE CONEXÃO COM BANCO
    except:

        #FUNÇÃO DE LIMPEZA DA TELA
        import Limpeza
        Limpeza.limpar()
        
        print('-=-'*10)
        print('CONEXÃO COM O BANCO - FALHA')
        print('-=-'*10)
        sleep(1)
        import Menu
        Menu.MenuPrincipal()
