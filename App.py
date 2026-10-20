import os

restaurantes = [{'nome':'praça', 'categoria':'japonesa', 'ativo':False}, {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True}, {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_do_programa():
    '''Essa função exibe o nome do programa'''
    
    print("""
╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╭━━━╮
┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱┃╭━━╯
┃╰━━┳━━┫╰━┳━━┳━╮┃╰━━┳╮╭┳━━┳━┳━━┳━━┳━━╮
╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯┃╭━━┻╋╋┫╭╮┃╭┫┃━┫━━┫━━┫
┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱┃╰━━┳╋╋┫╰╯┃┃┃┃━╋━━┣━━┃
╰━━━┻╯╰┻━━┻━━┻╯╱╰━━━┻╯╰┫╭━┻╯╰━━┻━━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯\n

""")

def exibir_opcoes():
    '''Essa função é resposavel a listar o cadastro do programa'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Essa função e responsavel a finaliz o programa'''
    exibir_subtitulos('Finalisar app')
    
def voltar_ao_menu_principal():
    ''' Essa função e resposavel a voltar ao menu apos usar uma função do programa'''
    input('\nDigite uma tecla para voltar ao menu  ')
    main() 

def opcao_invalida():
    '''Essa função e responsavel a invoformar quando uma opção for invalida'''
    print('opção invalida!\n')

    voltar_ao_menu_principal()

def exibir_subtitulos(texto):
    ''' essa função e responsavel em colocar *** em volta do testo do subtitulo'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsavel por cadastrar um novo restaurante
    inputs:

    - nome do restaurante
    - catedogria
    
    Outputs:
    - adiciona um novo restaurante a lista de restaurante
    
    '''
    exibir_subtitulos('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'digite o nome da categoria{nome_do_restaurante}:')
    print(f'O restaurante  {nome_do_restaurante} foi cadastrado com sucesso\n')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função e responsavel em cadastrar os restaurantes'''
    exibir_subtitulos('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo =  'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo} ')

    voltar_ao_menu_principal()  

def alternar_estado_restaurante():
    '''Essa função e responsavel em mudar o estado do restaurante
    
    Inputs:
    - nome do restaurante
    
    '''
    exibir_subtitulos('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante ['ativo'] else f'O restaurante{nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado: 
        print('O restaurante não foi encontrado')
        
def escolher_opcoes():
    '''Essa função e responsavel em  escolher as opções do programa
    
    Inputs: 
    - opção escolhida
    
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()  

def main():
    '''e responsavel pelo menu'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ =='__main__':
    main()