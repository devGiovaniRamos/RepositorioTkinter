import customtkinter as ctk
from lib import *

arquivo = r'D:\workspace\ws-VScode\RepositorioTkinter\ValidadorLogin\dados\BancoDeDados.txt'
if not arqExiste(arquivo):
    criarArq(arquivo)

#Personalização aparencia do app
ctk.set_appearance_mode('dark')
aplicativo = ctk.CTk()
aplicativo.title('Tela de Login')
aplicativo.geometry('300x300')

aplicativo.attributes(fullscreen=False)

#Botões e textos
login = ctk.CTkLabel(master=aplicativo, text='Usuário:')
login.pack(pady=5)
login_escrev = ctk.CTkEntry(aplicativo,placeholder_text='Digite seu usuário')
login_escrev.pack()
senha = ctk.CTkLabel(master=aplicativo, text='Senha:')
senha.pack(pady=5)
senha_escrev = ctk.CTkEntry(aplicativo,placeholder_text='Digite sua senha', show='*')
senha_escrev.pack()
resultado_login = ctk.CTkLabel(aplicativo, text='')

#Botão 'confirmar' e função de validação
botao = ctk.CTkButton(aplicativo, text='Confirmar', command=lambda: validar_user(login_escrev.get(), senha_escrev.get(), arquivo, resultado_login))
botao.pack(pady=5)

#Botão para finalizar programa
sair = ctk.CTkButton(aplicativo, text='Sair', command=aplicativo.destroy)
sair.pack(pady=5)
resultado_login.pack(pady=5)


aplicativo.mainloop()