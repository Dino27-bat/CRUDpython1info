usuario = dict({"lucas": {"nome": "lucas", "senha": "espinafre"}})

nome = str(input("Nome: "))

if(usuario.get(nome) != None):
    i_am = usuario[nome]
    senha = str(input("Senha: "))
    if(i_am['senha'] == senha):
        print("Logado")
    else:
        print("Erro")
else:
    print("Você não está cadastrado")