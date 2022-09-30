def cad():
    # if(bool(int(input('Usúario não encontrado!\nDeseja fazer o cadastro? [0-1]')))):

    conclu = False
    while (conclu == False):
        name = str(input("Digite seu nome: ")).title()
        senha = str(input("Digite sua senha: ")).encode('base64')
        if ():
            new_user = dict({name: {"NOME": name, "SENHA": senha}})
            conclu = True
            if (bool(int(input('Registro Feito!\nDeseja realizar o Login? [0-1]: ')))):
                print("Função de Login")
            else:
                print("Ok... Encerrando Programa.")
                exit()
        else:
            if (bool(int(input('Usúario já registrado! Deseja tentar novamente? [0-1]: ')))):
                print("Tente Novamente\n")
            else:
                conclu = True
                print("Ok... Encerrando Programa.")
                exit()
