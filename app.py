import os

restauranntes = [{'nome':'praça','categoria':'churras','ativo':False},
                 {'nome':'pizza','categoria':"Italiana",'ativo':True},
                 {'nome':'cantina','categoria':'Italiana','ativo':False}]


def cabeca():
    print("""
    █▀▄▀█ █▀▀ █▄░█ █░█   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀
    █░▀░█ ██▄ █░▀█ █▄█   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄\n""")

def mensagem():
    print('1 - Cadastrar Restaurantes')
    print('2 - Listar Restaurantes')
    print('3 - Ativar Restaurante')
    print('4 - Sair\n')

def subtitulos(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def finaliza():
    subtitulos('Saiu do Programa')

def voltar():
    input('\nPressione ENTER para continuar')
    main()


def opc_invalida():
    print('Opção invalida \n')
    voltar()

def cadastrar():
    '''  Função cadastrar Restaurantes '''
    subtitulos('Cadastrando Restaurante')
    nomer = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nomer}: ')
    dados_restaurante = {'nome': nomer, 'categoria': categoria, 'ativo': False}
    restauranntes.append(dados_restaurante)
    print(f'\nRestaurante {nomer} cadastrado com sucesso\n')
    voltar()

def listar():
    ''' Funçoo listar  e exibir restaurantes     '''
    subtitulos('Listando Restaurantes')
    print(f'    {'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Staus'}\n')
    for r in restauranntes:
        nome_res = r['nome']
        categoria = r['categoria']
        ativo = 'ativado' if r['ativo'] else 'desativado'
        print(f' -  {nome_res.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar()

def alternar_estado_rest():
    subtitulos('Alternar estado')
    nome_re = input('Digite o nome do restaurante que deseja alternar o status: ')
    restaurante_encontrado = False
    for r in restauranntes:
        if nome_re == r['nome']:
            restaurante_encontrado = True
            r['ativo'] = not r['ativo']
            mensagem = f'O restaurante {nome_re} foi ativado com sucesso' if r['ativo'] else f'O restaurante {nome_re} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    voltar()

def escolher_opc():
    try:
        opc = int(input('Digite um numero de 1 a 4: '))
        print(f'O numero escolhido foi {opc}')
        if opc == 1 : cadastrar()
        elif opc == 2 : listar()
        elif opc == 3 : alternar_estado_rest()
        elif opc == 4 : finaliza()
        else:
            opc_invalida()
    except:
        opc_invalida()

def main():
    os.system('cls')
    cabeca()
    mensagem()
    escolher_opc()


if __name__ == '__main__':
    main()

