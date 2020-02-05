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
    port = int(input('Digite a porta:'))
    db = str(input('Informe o banco:'))   
    print('-=-'*10)

    sleep(2)
    print('INICIANDO CONEXÃO...')
    sleep(2)
    print('CONECTANDO AO BANCO...\n')
    sleep(2)

    #TESTE DE CONEXÃO COM BANCO     
    try:    
        db = pymysql.connect(host, user, password, db, port)
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
            
            #MOSTRAR TODAS AS TABELAS
            print('-=-'*10)
            print('LISTAR TABELAS')
            print('-=-'*10)
            motb = 'SHOW TABLES'
            cursor.execute(motb)
            for x in cursor:
                print(x)
            db.close()
            criar_tabela()

        elif opc == 2:

            #FUNÇÃO DE LIMPEZA DA TELA
            import Limpeza
            Limpeza.limpar()
            
            #CRIAR NOVA TABELA
            print('-=-'*10)
            print('CRIAR TABELA')
            print('-=-'*10)
            nometb = str(input('Digite o nome do sua tabale:'))
            criartb = (f'CREATE TABLE {nometb}\n')
            
            sleep(1)
            print('CONECTANDO AO BANCO...')
            sleep(1)
            print(f'CRIANDO NOVA TABELA: {nometb}...')
            sleep(1)
            print(f'TABELA {nometb} CRIADA COM SUCESSO!\n')
            sleep(2)
            print('-=-'*10)
            cursor.execute(criartb)
            db.close()
            criar_tabela()

        elif opc == 3:
            
            #FUNÇÃO DE LIMPEZA DA TELA
            import Limpeza
            Limpeza.limpar()
            
            #EXCLUIR UMA TABELA
            print('-=-'*10)
            print('DELETAR TABELA')
            print('-=-'*10)
            nometb = str(input('Digite a tabela:'))
            detb = (f'DROP DATABASE {nometb}\n')
            
            sleep(1)
            print('CONECTANDO AO BANCO...')
            sleep(1)
            print(f'EXCLUINDO TABELA: {nometb}...')
            sleep(1)
            print(f'TABELA {nometb} EXCUIDA COM SUCESSO!\n')
            sleep(2)
            print('-=-'*10)
            cursor.execute(detb)
            db.close()
            criar_tabela()

        elif opc == 4:
            
            #FUNÇÃO DE LIMPEZA DA TELA
            import Limpeza
            Limpeza.limpar()
            
            #VOLTAR PARA MENU ANTERIOR
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
