def MenuPrincipal():

      print('-=-'*10)
      print('CRIADOR DE BANCO DE DADOS')
      print('-=-'*10)

      print('[1] TESTE DE BANCO\n'
            '[2] CRIAR BANCO\n'                 
            '[3] CRIAR TABELA\n'
            '[4] SAIR\n')
      opc = int(input('-->'))
    
      if opc == 1:
            import TesteBanco
            TesteBanco.teste_banco()
      elif opc == 2:
            import CriarBanco
            CriarBanco.criar_banco()
      #elif opc == 3:
      #      criar_tabela()
      elif opc == 4:
            exit

MenuPrincipal()