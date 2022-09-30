rodando = True

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
    resposta = menu(['Logar', 'hakis', 'aaa'])
    if resposta == 1:
        login()
        break
    elif resposta == 2:
        cabeçalho('Opção 2')
        break
    elif resposta == 3:
        cabeçalho('\033[36mSaindo do sistema... Até logo!\033[m')
        exit()
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[32m')
