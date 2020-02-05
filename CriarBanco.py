import pymysql # para o MySQL
from time import sleep
import Menu
import Limpeza
import CriarBanco
import Layout
#-----------------------------------------------------------------
#MANIPULAÇÃO DE BANCO
#-----------------------------------------------------------------
def menu_banco():
#-----------------------------------------------------------------
    #FUNÇÃO DE LIMPEZA DA TELA
    Limpeza.limpar()
    Layout.linha()
    print('MENU - BANCO DE DADOS')
    Layout.linha()
#-----------------------------------------------------------------
    host = str(input('Digite o ip:'))         
    user = str(input('Digite o usuário:'))         
    password = str(input('Digite a password:'))   
    Layout.linha()
    sleep(2)
    print('INICIANDO CONEXÃO...')
    sleep(2)
    print('CONECTANDO AO BANCO...\n')
    sleep(2) 
#-----------------------------------------------------------------
    try:
        #CHAMADA DA CONEXÃO DO BANCO    
        db = pymysql.connect(host, user, password)
        cursor = db.cursor()
        Layout.linha()
        print('CONEXÃO COM O BANCO - OK')
        Layout.linha()
        sleep(1)
#-----------------------------------------------------------------
        #LISTAR BANCOS EXISTENTES
        Layout.linha()
        modb = 'SHOW DATABASES'
        cursor.execute(modb)
        print('|TODOS OS BANCOS     |')
        print('-' * 22)
        for x in cursor:
            x = list(x) #CONVERTENDO TULIPAS EM LISTA
            x = str(x).strip('[]') #CONVERTENDO LISTA EM STRINGS E REMOVENDO OS COLCHETES 
            print(f'|{x.rstrip().rjust(4).ljust(20).upper()}|') #PRINT FORMATADO DOS BANCOS
        Layout.linha()
#-----------------------------------------------------------------
        #MENU DE ESCOLHAR
        print('[1] CRIAR BANCOS\n'                 
              '[2] DELETAR BANCOS\n'
              '[3] VOLTAR\n')
        opc = int(input('-->'))
#-----------------------------------------------------------------  
        if opc ==1:
            #FUNÇÃO DE LIMPEZA DA TELA
            Limpeza.limpar()

            Layout.linha()
            print('CRIAR - BANCO DE DADOS')
            Layout.linha()

            nomedb = str(input('Digite o nome do seu Banco:'))
            criardb = (f'CREATE DATABASE {nomedb}\n')
                    
            sleep(1)
            print('CONECTANDO AO BANCO...')
            sleep(1)
            print(f'CRIANDO NOVO BANCO DE DADOS: {nomedb}...')
            sleep(1)
            print(f'BANCO DE DADOS {nomedb} CRIADO COM SUCESSO!\n')
            sleep(2)
            Layout.linha()
            cursor.execute(criardb)
            db.close()
            menu_banco()
#-----------------------------------------------------------------
        elif opc == 2:
           #FUNÇÃO DE LIMPEZA DA TELA
            Limpeza.limpar()
                
            Layout.linha()
            print('DELETAR - BANCO DE DADOS')
            Layout.linha()
            print('DESEJA MOSTRAR TODOS OS BANCOS?\n'                 
            '[1] SIM\n')
            opc = int(input('-->'))

            if opc == 1:
                #LISTAR BANCOS EXISTENTES
                Layout.linha()
                print('LISTAR BANCOS')
                Layout.linha()
                modb = 'SHOW DATABASES'
                cursor.execute(modb)
                print('|BANCOS              |')
                print('-' * 22)
                for x in cursor:
                    x = list(x) #CONVERTENDO TULIPAS EM LISTA
                    x = str(x).strip('[]') #CONVERTENDO LISTA EM STRINGS E REMOVENDO OS COLCHETES 
                    print(f'|{x.rstrip().rjust(4).ljust(20).upper()}|') #PRINT FORMATADO DOS BANCOS
                
            Layout.linha()
            nomedb = str(input('Digite o Banco:'))
            dedb = (f'DROP DATABASE {nomedb}\n')        
            sleep(1)
            print('CONECTANDO AO BANCO...')
            sleep(1)
            print(f'EXCLUINDO BANCO DE DADOS: {nomedb}...')
            sleep(1)
            print(f'BANCO DE DADOS {nomedb} EXCUIDO COM SUCESSO!')
            sleep(2)
            Layout.linha()
            cursor.execute(dedb)
            db.close()
            menu_banco()
#-----------------------------------------------------------------
        elif opc == 3:
            #FUNÇÃO DE LIMPEZA DA TELA
            Limpeza.limpar()
                
            print('VONTANDO PARA O MENU PINCIPAL')
            sleep(1)
            Menu.MenuPrincipal()  
#-----------------------------------------------------------------        
    #QUANDO FALHAR O TEXTE DE CONEXÃO COM BANCO
    except:
        #FUNÇÃO DE LIMPEZA DA TELA
        Limpeza.limpar()
        
        Layout.linha()
        print('CONEXÃO COM O BANCO - FALHA')
        Layout.linha()
        sleep(1)
        Menu.MenuPrincipal()
#-----------------------------------------------------------------


#-------------------------CÓDIGO ANTIGO---------------------------
'''
# MANIPULAÇÃO DE BANCO
def criar_ba():
    
    #FUNÇÃO DE LIMPEZA DA TELA
    import Limpeza
    Limpeza.limpar()
    
    print('-=-'*10)
    print('CRIADOR DE BANCO DE DADOS')
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
        print('[1] LISTAR BANCOS\n'
              '[2] CRIAR BANCOS\n'                 
              '[3] DELETAR BANCOS\n'
              '[4] VOLTAR\n')
        opc = int(input('-->'))

        if opc == 1:
            
            #FUNÇÃO DE LIMPEZA DA TELA
            import Limpeza
            Limpeza.limpar()

            print('-=-'*10)
            print('LISTAR BANCOS')
            print('-=-'*10)
            modb = 'SHOW DATABASES'
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
'''
#-------------------------CÓDIGO ANTIGO---------------------------