import pymysql
import CriarBanco
import Limpeza
import TesteBanco
import CriarTabela


# MENU PRINCIPAL DO PROGRAMA
def MenuPrincipal():
    Limpeza.limpar()

    print('-=-' * 10)
    print('CRIADOR DE BANCO DE DADOS')
    print('-=-' * 10)

    print('\n')  # ESAÇO

    print('[1] TESTE DE BANCO\n'
          '[2] CRIAR BANCO\n'
          '[3] CRIAR TABELA\n'
          '[4] SAIR\n')
    opc = int(input('-->'))

    if opc == 1:
        TesteBanco.teste_banco()

    elif opc == 2:
        CriarBanco.menu_banco()

    elif opc == 3:
        CriarTabela.criar_tabela()

    elif opc == 4:
          exit()
