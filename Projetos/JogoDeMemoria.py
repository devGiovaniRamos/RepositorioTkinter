from tkinter import *
import tkinter.messagebox as messagebox
import random

#definindo configs do jogo
num_linhas = 4
num_colunas = 4
cartao_size_w = 10
cartao_size_h = 5
colors_cart = ['red', 'yellow', 'blue', 'white', 'green', 'orange', 'purple', 'cyan']
color_fund = '#474747'
color_letra = '#ffffff'
font_letra = ('Backso', 12)
max_tentativas = 20 

#grade aleatória de cores para cartões
def create_card_grid():
    cores = colors_cart *2
    random.shuffle(cores)
    grid = []

    for _ in range(num_linhas):
        linha = []
        for _ in range(num_colunas):
            cor = cores.pop()
            linha.append(cor)
        grid.append(linha)
    return grid

#clique do jogador
def clique(linha, coluna):
    cartao = cartoes[linha][coluna]
    cor = cartao['bg']
    if cor=='#6b6b6b':  
        cartao['bg'] = grid[linha][coluna]
        cartao_revelado.append(cartao)
        if len(cartao_revelado) == 2:
            check_math()

#verificando se cartões sao iguais
def check_math():
    carta1, carta2 = cartao_revelado
    if carta1['bg'] == carta2['bg']:
        carta1.after(1000, carta1.destroy)
        carta2.after(1000,carta2.destroy)
        cartao_correspondentes.extend([carta1, carta2])
        check_win()
    else:
        carta1.after(1000, lambda:carta1.config(bg='#6b6b6b'))
        carta2.after(1000, lambda:carta2.config(bg='#6b6b6b'))
    cartao_revelado.clear()
    update_score()

#verificar se o jogador ganhou
def check_win():
    if len(cartao_correspondentes) == num_linhas * num_colunas:
        messagebox.showinfo('PARABÉNS!', 'Você encontrou todos os pares.')
        janela.quit

#Atualizar pontuação
def update_score():
    global num_tentativas
    num_tentativas += 1
    label_tentativas.configure(text='Tentativas: {}/{}'.format(num_tentativas, max_tentativas))
    if num_tentativas >= max_tentativas:
        messagebox.showinfo('Fim de Jogo', 'Você perdeu')
        janela.quit



                                                  #PROGRAMA PRINCIPAL

#criando interface principal
janela = Tk()
janela.title('Jogo de Memória')
janela.configure(bg=color_fund)

#grade de cartões
grid = create_card_grid()
cartoes = []
cartao_revelado = []
cartao_correspondentes = []
num_tentativas = 0
for linha in range(num_linhas):
    linha_de_cartoes = []
    for coluna in range(num_colunas):
        cartao = Button(janela, command=lambda r=linha, c=coluna: clique(r, c),width=cartao_size_w, height=cartao_size_h, bg='#6b6b6b', relief=RAISED, bd=3)
        cartao.grid(row=linha, column=coluna, padx=5, pady=5)
        linha_de_cartoes.append(cartao)
    cartoes.append(linha_de_cartoes)


#personalizando botão
button_style = {'activebackground' : 'f8f9fa', 'font': font_letra, 'fg': color_letra}
janela.option_add('*Button', button_style)

#label número de tentativas
label_tentativas = Label(janela, text='Tentativas: {}/{}'.format(num_tentativas, max_tentativas), fg=color_letra, bg=color_fund, font=font_letra)
label_tentativas.grid(row=num_linhas, columnspan=num_colunas, padx=10, pady=10)


janela.mainloop()