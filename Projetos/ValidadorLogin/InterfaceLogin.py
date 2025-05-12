import customtkinter as ctk
from lib import *

arquivo = r'D:\workspace\ws-VScode\RepositorioTkinter\Projetos\ValidadorLogin\dados\BancoDeDados.txt'
if not arqExiste(arquivo):
    criarArq(arquivo)

#Personalização aparencia do app
ctk.set_appearance_mode('dark')
aplicativo = ctk.CTk()
aplicativo.title('Tela de Login/Cadastro')
aplicativo.geometry('300x300')
aplicativo.attributes(fullscreen=False)

#Botões e textos
login = ctk.CTkLabel(master=aplicativo, text='Usuário:')
login.pack(pady=5)
login_esc = ctk.CTkEntry(aplicativo,placeholder_text='Digite seu usuário')
login_esc.pack()
senha = ctk.CTkLabel(master=aplicativo, text='Senha:')
senha.pack(pady=5)
senha_esc = ctk.CTkEntry(aplicativo,placeholder_text='Digite sua senha', show='*')
senha_esc.pack()
resultado_login = ctk.CTkLabel(aplicativo, text='')

#Botão confirmar
botao = ctk.CTkButton(aplicativo, text='Confirmar', command=lambda:
                       validar_user(login_esc.get(), senha_esc.get(), arquivo, resultado_login))
botao.pack(pady=5)

#Botão cadastrar_se
cadastrar_se = ctk.CTkButton(aplicativo, text='Cadastrar-se', command=lambda:
                         cadastrar(login_esc, senha_esc, arquivo, resultado_login))
cadastrar_se.pack(pady=5)

#Botão para finalizar programa
sair = ctk.CTkButton(aplicativo, text='Sair', command=aplicativo.destroy)
sair.pack(pady=5)

resultado_login.pack(pady=5)



aplicativo.mainloop()
