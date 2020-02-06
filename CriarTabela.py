import pymysql # para o MySQL
from time import sleep
import Layout
import Limpeza
#-----------------------------------------------------------------
# MANIPULAÇÃO DE TABELAS
def criar_tabela():
    
    #FUNÇÃO DE LIMPEZA DA TELA
    Limpeza.limpar()
    
    Layout.linha()
    print('CRIADOR DE TABELA')
    Layout.linha()

    #COLETANDO INFORMAÇÕES DE CONEXÃO DO BANCO
    host = str(input('Digite o ip:'))         
    user = str(input('Digite o usuário:'))         
    password = str(input('Digite a password:'))
    db = pymysql.connect(host, user, password)
    cursor = db.cursor()
    #LISTAR BANCOS EXISTENTES
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
    db = str(input('Informe o banco:')) 
    port = int(input('Digite a porta:'))
    Layout.linha()

    sleep(2)
    print('INICIANDO CONEXÃO...')
    sleep(2)
    print('CONECTANDO AO BANCO...\n')
    sleep(2)
#-----------------------------------------------------------------
    #TESTE DE CONEXÃO COM BANCO     
    try:    
        db = pymysql.connect(host, user, password, db, port)
        cursor = db.cursor()  
        Layout.linha()
        print('CONEXÃO COM O BANCO - OK')
        Layout.linha()
        sleep(1)

        #MOSTRAR TODAS AS TABELAS
        Layout.linha()
        motb = 'SHOW TABLES'
        cursor.execute(motb)
        print('|TODAS AS TABELAS    |')
        print('-' * 22)
        for x in cursor:
            x = list(x) #CONVERTENDO TULIPAS EM LISTA
            x = str(x).strip('[]') #CONVERTENDO LISTA EM STRINGS E REMOVENDO OS COLCHETES 
            print(f'|{x.rstrip().rjust(4).ljust(20).upper()}|') #PRINT FORMATADO DOS BANCOS
        Layout.linha()
        #FUNÇÃO DE LIMPEZA DA TELA
        Limpeza.limpar()
        
        print('[1] CRIAR TABELA\n'                 
              '[2] DELETAR TABELA\n'
              '[3] VOLTAR\n')
        opc = int(input('-->'))
#-----------------------------------------------------------------        
        if opc == 0:
            
            #FUNÇÃO DE LIMPEZA DA TELA
            Limpeza.limpar()
         
            #MOSTRAR TODAS AS TABELAS
            Layout.linha()
            print('LISTAR TABELAS')
            Layout.linha()
            motb = 'SHOW TABLES'
            cursor.execute(motb)
            print('|TODAS AS TABELAS    |')
            print('-' * 22)
            for x in cursor:
                x = list(x) #CONVERTENDO TULIPAS EM LISTA
                x = str(x).strip('[]') #CONVERTENDO LISTA EM STRINGS E REMOVENDO OS COLCHETES 
                print(f'|{x.rstrip().rjust(4).ljust(20).upper()}|') #PRINT FORMATADO DOS BANCOS
            db.close()
            criar_tabela()
#-----------------------------------------------------------------
        elif opc == 1:

            #FUNÇÃO DE LIMPEZA DA TELA
            Limpeza.limpar()
            
            #CRIAR NOVA TABELA
            Layout.linha()
            print('CRIAR TABELA')
            Layout.linha()
            nometb = str(input('Digite o nome do sua tabale:'))
            criartb = (f'CREATE TABLE {nometb}\n')
            
            sleep(1)
            print('CONECTANDO AO BANCO...')
            sleep(1)
            print(f'CRIANDO NOVA TABELA: {nometb}...')
            sleep(1)
            print(f'TABELA {nometb} CRIADA COM SUCESSO!\n')
            sleep(2)
            Layout.linha()
            cursor.execute(criartb)
            db.close()
            criar_tabela()
#-----------------------------------------------------------------
        elif opc == 2:
            
            #FUNÇÃO DE LIMPEZA DA TELA
            Limpeza.limpar()
            
            #EXCLUIR UMA TABELA
            Layout.linha()
            print('DELETAR TABELA')
            Layout.linha()
            print('DESEJA MOSTRAR TODAS AS TABELAS?\n'                 
            '[1] SIM\n')
            opc = int(input('-->'))

            if opc == 1:
                #MOSTRAR TODAS AS TABELAS
                Layout.linha()
                print('LISTAR TABELAS')
                Layout.linha()
                motb = 'SHOW TABLES'
                cursor.execute(motb)
                print('|TODAS AS TABELAS    |')
                print('-' * 22)
                for x in cursor:
                    x = list(x) #CONVERTENDO TULIPAS EM LISTA
                    x = str(x).strip('[]') #CONVERTENDO LISTA EM STRINGS E REMOVENDO OS COLCHETES 
                    print(f'|{x.rstrip().rjust(4).ljust(20).upper()}|') #PRINT FORMATADO DOS BANCOS
                
            
            Layout.linha()
            nometb = str(input('Digite a tabela:'))
            detb = (f'DROP DATABASE {nometb}\n')
            sleep(1)
            print('CONECTANDO AO BANCO...')
            sleep(1)
            print(f'EXCLUINDO TABELA: {nometb}...')
            sleep(1)
            print(f'TABELA {nometb} EXCUIDA COM SUCESSO!\n')
            sleep(2)
            Layout.linha()
            cursor.execute(detb)
            db.close()
            criar_tabela()
#-----------------------------------------------------------------
        elif opc == 3:
            
            #FUNÇÃO DE LIMPEZA DA TELA
            Limpeza.limpar()
            
            #VOLTAR PARA MENU ANTERIOR
            print('VONTANDO PARA O MENU PINCIPAL')
            sleep(1)
            db.close()
            import Menu
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
        import Menu
        Menu.MenuPrincipal()
#-----------------------------------------------------------------