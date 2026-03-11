import os

contatos = []

def nome_programa():
    print('MEUS CONTATOS')


def menu():
    print('1- Adicionar contato')
    print('2- Listar Contatos')
    print('3- Buscar Contato')
    print('4- Remover Contato')
    print('5- Sair')

def voltar_ao_menu():
    input('Digite qualquer tecla para voltar ao menu')
    os.system('cls')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)


def adicionar_contato():
    exibir_subtitulo('Adicionar Contato')
    contato = input('Nome:')
    telefone = input('Telefone:')
    informacoes = {'Nome': contato , 'Telefone': telefone}
    contatos.append(informacoes)
    print('Contato Adicionado com sucesso!\n')
    voltar_ao_menu()


def listar_contatos():
    exibir_subtitulo('Listar Contatos')

    if not contatos:
        print('Voce ainda nao tem nenhum contato')
    else:
        for chave in contatos:
            nome_contato = chave['Nome']
            numero_telefone = chave['Telefone']
            print(f'- {nome_contato} | Tel: {numero_telefone}')

    voltar_ao_menu()
      
def buscar_contato():
    exibir_subtitulo('Buscar Contato')
    nome = input('Digite o nome que voce deseja buscar:')
    for chave in contatos:
        if nome == chave['Nome']:
            print(f'Informacoes sobre {nome}:')
            print(chave['Nome'], '|', chave['Telefone'],'\n')   
    voltar_ao_menu()

def remover_contato():
    exibir_subtitulo('Remover Contato')
    contato = input('Digite o contato que voce deseja remover:')
    for chave in contatos:
        if contato == chave['Nome']:
            contatos.remove(chave)
            print(f'Usuario {contato} removido com sucesso!')
            voltar_ao_menu()
            return
    print('Usuario nao encontrado')
    voltar_ao_menu()


def encerrar_programa():
    os.system('cls')
    print('Programa Finalizado')


def escolher_opcao ():
    try:
        opcao = int(input('Selecione uma opcao:'))
        if opcao == 1:
            adicionar_contato()
        elif opcao == 2:
            listar_contatos()
        elif opcao == 3:
            buscar_contato()
        elif opcao == 4:
            remover_contato()
        elif opcao == 5:
            encerrar_programa()
        else:
            os.system('cls')
            print('Digite uma das opcoes possiveis')
            voltar_ao_menu()
    except ValueError:
        os.system('cls')
        print('Voce nao digitou uma das opcoes')
        voltar_ao_menu()

def main():
    nome_programa()
    menu()
    escolher_opcao()


if __name__ == '__main__':
    main()
