from tkinter import *
from tkinter import ttk

#Olá Mundo!
janela = Tk()
janela.title('Olá Mundo')
ttk.Label(text="Hello World!").grid(column=0, row=0)
ttk.Button(text="Quit", command=janela.destroy).grid(column=1, row=0)

janela.mainloop()