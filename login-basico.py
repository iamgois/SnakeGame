usuario = input('Usuario: ')
senha = input('Senha: ')

msg_bemvindo = "Bem vindo!"
usuario_db = ("Thiago")
senha_db = ("123456")

if usuario == usuario_db and senha == senha_db:
    print(f'Bem Vindo {usuario:#^20}')
else:
    print('Usuário ou senha incorreto...')