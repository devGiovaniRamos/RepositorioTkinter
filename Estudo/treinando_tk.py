from tkinter import *

#Olá Mundo!
janela = Tk()
janela.title('Criando meu primeiro Olá Mundo usando tk')
janela.configure(bg='#6b6b6b')
menuBar = Menu(janela)
#estava estudando sobre o menu
janela.config(menu=menuBar)

janela.mainloop()