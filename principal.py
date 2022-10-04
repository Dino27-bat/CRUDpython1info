usuarios = dict(
    {
        "lucas_zebool@pa.com":
        {
            "NOME": "Lucas",
            "TYPE_U": int(0),
            "EMAIL": "lucas_zebool@pa.com",
            "SENHA": "espinafre",
            "SALARIO": float(12000),
            "C_HORARIA_D": int(8)
        }
    })

#TYPE_U
#[0] - Chefe
#[1] - Funcionario

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

    email = str(input("Email: "))
    while ('@' not in email):
        email = str(input("Por favor, Digite um email válido: "))
    tentativas = int(3)

    if (usuarios.get(email) != None):
        usuario_2 = usuarios.get(email)
        usuario_2['KEY'] = email
        while (tentativas >= 0): 
            if (usuario_2['SENHA'] == str(input("Senha: "))):
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
        email = str(input("Digite sua email: "))
        while ('@' not in email):
            email = str(input("Por favor, Digite um email válido: "))
        senha = str(input("Digite sua senha: "))

        if (usuarios.get(email) == None):
            usuarios.update(
                dict(
                    {email:
                     {
                         "NOME": name,
                         "TYPE_U": int(1),
                         'EMAIL': email,
                         "SENHA": senha,
                         "SALARIO": float(2812),
                         "C_HORARIA_D": int(6)
                     }}))
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


def showInfos(other=None):
    global logged
    if (other == None):
        print(
            "Nome: ", logged['NOME'],
            "\nTipo de Funcionário: ", logged['TYPE_U'],
            "\nEmail: ", logged['EMAIL'],
            "\nSalário: ", logged['SALARIO'],
            "\nCarga horária Diária: ", logged['C_HORARIA_D'],
            "\nCarga horária Semanal: ", int(logged['C_HORARIA_D'] * 6))
    else:
        print(
            "Nome: ", other['NOME'],
            "\nTipo de Funcionário: ", other['TYPE_U'],
            "\nEmail: ", other['EMAIL'],
            "\nSalário: ", other['SALARIO'],
            "\nCarga horária Diária: ", other['C_HORARIA_D'],
            "\nCarga horária Semanal: ", int(other['C_HORARIA_D'] * 6))


def delete():
    global logged

    senha = str(input("Digite sua senha: "))
    tentativa = int(3)
    while tentativa >= 0:
        if senha == logged['SENHA']:
            usuarios.pop(logged['KEY'])
            logged = None
            print("Conta Deletada...")
            print(usuarios)
            break
        else:
            print("Senha incorreta!")
            tentativa -= 1


def altern():
    global logged

    if (logged['TYPE_U'] == 0 and bool(leiaInt('Deseja alterar os dados de outros funcionários? [0-1]: '))):
        print("Lista de funcionários")

        index_users_k = list(usuarios.keys())
        index_users = int(0)

        for x in usuarios.values():
            print("[", index_users, "] -> ", x['NOME'], " - ", x['EMAIL'])
            index_users += 1

        index_users = leiaInt('Qual funcionário deseja alterar: ')
        index_users_k = usuarios[index_users_k[index_users]]
        showInfos(index_users_k)

        to_altern = leiaInt("""
        O que deseja alterar?
        [1] - Nome
        [2] - Cargo
        [3] - Salário
        [4] - Carga Horária Diária
        """)

        match to_altern:
            case 1:
                index_users_k['NOME'] = str(input('Digite o Nome: '))
            case 2:
                index_users_k['TYPE_U'] = leiaInt("""
                Cargo:
                [0] - Chefe
                [1] - Funcionário
                """)
            case 3:
                index_users_k['SALARIO'] = float(input('Salário: '))
            case 4:
                index_users_k['C_HORARIA_D'] = leiaInt('Carga Horária Diária: ')
        
        usuarios[index_users_k['EMAIL']] = index_users_k
    else:
        to_altern = leiaInt("""
        O que deseja alterar?
        [1] - Nome
        [2] - Email
        [3] - Senha
        """)

        match to_altern:
            case 1:
                logged['NOME'] = str(input('Digite o Nome: '))
            case 2:
                email = str(input("Email: "))
                while ('@' not in email):
                    email = str(input("Por favor, Digite um email válido: "))
                logged['EMAIL'] = email
            case 3:
                logged['SENHA'] = str(input('Senha: '))

        usuarios[logged['EMAIL']] = usuarios.pop(logged['KEY'])
        logged['KEY'] = logged['EMAIL']
        


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
        if logged != None:
            if logged['TYPE_U'] == 0:
                cabeçalho('MENU PRINCIPAL (Chefe)')
            else:
                cabeçalho('MENU PRINCIPAL (Funcionário)')
        else:
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
            resposta = menu(['Alterar', 'Apagar', 'Informações',
                            'Deslogar', 'Sair Da Aplicação'])
            print()
            if resposta == 1:
                altern()
                break
            elif resposta == 2:
                delete()
                break
            elif resposta == 3:
                showInfos()
                break
            elif resposta == 4:
                logged = None
                cabeçalho('\033[36mVocê Deslogou da sua Conta\033[m')
                break
            elif resposta == 5:
                cabeçalho('\033[36mSaindo do sistema... Até logo!\033[m')
                exit()
            else:
                print('\033[31mERRO! Digite uma opção válida!\033[32m')
        else:
            resposta = menu(['Logar', 'Cadastrar', 'Sair Da Aplicação'])

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