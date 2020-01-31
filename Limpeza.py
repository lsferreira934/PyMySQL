# SISTEMA PARA DAR LIMPEZA DE TELA 
def limpar():
    import sys
    # Pega qual é o SO
    so = sys.platform
    so_clear = ''

    # Defini o argumento para limpeza de tela de acordo com o SO
    if (so == 'linux'):
        so_clear = 'clear'
    elif (so[:3] == 'win'):
        so_clear = 'cls'

    # Função lambda para limpeza de tela
    if so_clear:
        limpar = lambda l: os.system(l)
    else:
        limpar = lambda l: l
#-------------------------------------------------------------------------