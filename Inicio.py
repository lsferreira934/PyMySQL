print('\n\n')
print('by Leandro Ferreira')
print('-=' * 45)
print('\t\t\t### BEM VINDO AO CRIADO DE BANCO DE DADOS ###\n')
print('\t\t\t\t\tWARNING!!\n')
print('\t\t*CERTIFIQUE - SE DE TER INSTALADO OS SEGUINTES PROGRAMAS:')
print('\t\tXAMPP: https://www.apachefriends.org/pt_br/download.html\n')
print('\t\t*RECOMENDAMOS A INSTALANÇÃO TAMBEM DA FERRAMENTE MYSQL - WORKBENCH')
print('\t\tWORKBENCH: https://dev.mysql.com/downloads/workbench/\n')
print('\t\t\t\t[1] INICIAR  [2] SAIR\n')
opc = int(input('\t\t\t\t------> '))
print('-=' * 45)

print('\n\n')

if opc == 1:
    import Menu
    Menu.MenuPrincipal()
else:
    exit