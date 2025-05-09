def arqExiste(nome):
    """
    Verifica se existe o arquivo para guardar dados
    """
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


def cadastrar(login, senha, arquivo, resultado_login):
    """
    função para obter usuário e login digitados e guardar no arquivo txt
    """
    import customtkinter as ctk
    login_ = login.get()
    senha_ = senha.get()
    if not login_ or not senha_:
        resultado_login.configure(text='Nenhum usuário cadastrado', text_color='white')
    else:
        novo_usuario = login_
        nova_senha = senha_
        try:
            with open(arquivo, 'a') as arq:
                arq.write(f'{novo_usuario};{nova_senha}\n')
            resultado_login.configure(text='Usuário cadastrado com sucesso!', text_color='yellow')
        except Exception as e:
            resultado_login.configure(text=f'Erro ao cadastrar: {e}', text_color='red')
    login.delete(0, ctk.END)
    senha.delete(0, ctk.END)
  

def validar_user(login, senha, arquivo, resultado_login):
    """
    função de validação para a interface;
    retorna True caso seja válido o login
    """
    try:
        arq = open(arquivo, 'rt')
        for l in arq:
            usuario_armazenado, senha_armazenada = l.strip().split(';')
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

