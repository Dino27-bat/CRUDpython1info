usuario = dict({"Lucas": {"NOME": "Lucas", "TYPE_U": "ADM", "SENHA": "espinafre"}})

logged = None


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError):
            print(
                '\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('Usúario preferiu nâo digitar esse número.')
            return 0
        else:
            return n


def login():
    global logged

    nome = str(input("Nome: "))
    tentativas = int(3)

    if (usuario.get(nome) != None):
        usuario_2 = usuario.get(nome)
        usuario_2['KEY'] = nome
        while (tentativas >= 0):
            senha = str(input("Senha: "))
            if (usuario_2['SENHA'] == senha):
                logged = usuario_2
                return print("Logado")
            else:
                print("Erro! Tentativas Restantes: ", tentativas)
                tentativas -= 1

        return print("Você excedeu o Número de Tentativas")
    else:
        return print("Você não está cadastrado!")


def cad():

    conclu = False
    while (conclu == False):
        name = str(input("Digite seu nome: "))
        senha = str(input("Digite sua senha: "))
        if (usuario.get(name) == None):
            usuario.update(dict({name: {"NOME": name, "TYPE_U": "CLIENT" ,"SENHA": senha}}))
            conclu = True
            if (bool(leiaInt('Registro Feito!\nDeseja realizar o Login? [0-1]: '))):
                login()
            else:
                print("Ok... Voltando ao Menu Principal\n")
                options()
        else:
            if (bool(leiaInt('Usúario já registrado! Deseja tentar novamente? [0-1]: '))):
                cad()
            else:
                conclu = True
                print("Ok... Voltando ao Menu Principal\n")
                options()

def showInfos():
    print(
        "Nome: ", logged['NOME'], 
        "\nTipo de Usúario: ", logged['TYPE_U'])

def delete():
    global logged

    senha = str(input("Digite sua senha: "))
    tentativa = int(3)
    while tentativa >= 0:
        if senha == logged['SENHA']:
            usuario.pop(logged['KEY'])
            logged = None
            print("Conta Deletada...")
            print(usuario)
            break
        else:
            print("Senha incorreta!")
            tentativa -= 1

def options():
    global logged   
    rodando = True

    def linha(tam=42):
        return '-' * tam

    def cabeçalho(txt):
        print(linha())
        print(txt.center(42))
        print(linha())

    # Menu

    def menu(lista):
        cabeçalho('MENU PRINCIPAL')
        c = 1
        for item in lista:
            print(f'\033[33m {c} \033[m - \033[34m {item} \033[m')
            c += 1
        print(linha())
        opc = leiaInt('\033[32mSua Opção: \033[m')
        return opc

    # Codigo Principal
    while rodando == True:
        if logged != None:
            resposta = menu(['Alterar', 'Apagar', 'Informações', 'Sair'])
            print()
            if resposta == 1:
                #altern()
                break
            elif resposta == 2:
                delete()
                break
            elif resposta == 3:
                showInfos()
                break
            elif resposta == 4:
                cabeçalho('\033[36mSaindo do sistema... Até logo!\033[m')
                exit()
            else:
                print('\033[31mERRO! Digite uma opção válida!\033[32m')
        else:
            resposta = menu(['Logar', 'Cadastrar', 'Sair'])

            if resposta == 1:
                login()
                break
            elif resposta == 2:
                cad()
                break
            elif resposta == 3:
                cabeçalho('\033[36mSaindo do sistema... Até logo!\033[m')
                exit()
            else:
                print('\033[31mERRO! Digite uma opção válida!\033[32m')

while True:
    options()  