def arqExiste(nome):
    try:
        a=open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArq(nome):
    try:
        a=open(nome, 'wt+')
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo ({nome}) criado com sucesso.')



def validar_user(login, senha, arquivo, resultado_login):
    try:
        arq = open(arquivo, 'rt')
        for l in arq:
            usuario_armazenado, senha_armazenada = l.strip().split(':')
            if usuario_armazenado == login:
                if senha_armazenada == senha:
                    resultado_login.configure(text='Login feito com sucesso.', text_color='green')
                    return True
                else:
                    resultado_login.configure(text='Usuário ou senha inválidos.', text_color='red')
                    return False 
        resultado_login.configure(text='Usuário ou senha inválidos.', text_color='red')
        return False 
    except FileNotFoundError:
        resultado_login.configure(text='Erro ao acessar o arquivo de usuários.', text_color='red')
        return False

