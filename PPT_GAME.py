# -- Importação da interface grafica ----------
import tkinter
from tkinter import *
from tkinter import ttk

# Importando o Pillow --------------------------
from PIL import Image, ImageTk

import random
# cores ----------------------------------------
co0 = "#3B3B3B"  # Gray 1
co1 = "#333333"  # Gray 2
co2 = "#fcc058"  # orange
co3 = "#ED9234"  # yellow
co4 = "#20C997"  # green
co5 = "#ED6F4C"  # red
co6 = "#fcc058"  # orange
co7 = "#e85151"  # vermelha
co8 = "#34eb3d"  # green 02
fundo = "#3b3b3b"
# configurando a janela -------------------------
janela = Tk()
janela.title('Pedra, Papel, Tesoura')
janela.geometry('260x280')
janela.configure(bg=fundo)

# dividindo a janela -----------------------------

frame_cima = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW)

frame_baixo = Frame(janela, width=260, height=180, bg=co0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Configurando o frame_cima -----------------------

# -- Tudo que é relacionado ao jogador 01 é o 'app_1'
app_1 = Label(frame_cima, text='Você', height=1, anchor='center', font='Ivy 10 bold', bg=co1, fg='white')
app_1.place(x=25, y=70)

app_1_linha = Label(frame_cima, text='', height=10, anchor='center', font='Ivy 10 bold', bg=co0, fg='white')
app_1_linha.place(x=0, y=0)

app_1_pontos = Label(frame_cima, text='0', height=1, anchor='center', font='Ivy 30 bold', bg=co1, fg='white')
app_1_pontos.place(x=50, y=20)
# ----------------------------------------------------

# -- Tudo que é relacionado a separação de oponentes
app_ = Label(frame_cima, text=':', height=1, anchor='center', font='Ivy 30 bold', bg=co1, fg='white')
app_.place(x=125, y=20)
# ----------------------------------------------------

# -- Tudo que é relacionado ao jogador 02 é o 'app_2'
app_2_pontos = Label(frame_cima, text='0', height=1, anchor='center', font='Ivy 30 bold', bg=co1, fg='white')
app_2_pontos.place(x=170, y=20)

app_2 = Label(frame_cima, text='PC', height=1, anchor='center', font='Ivy 10 bold', bg=co1, fg='white')
app_2.place(x=205, y=70)

app_2_linha = Label(frame_cima, text='', height=10, anchor='center', font='Ivy 10 bold', bg=co0, fg='white')
app_2_linha.place(x=255, y=0)
# ----------------------------------------------------

# -- Tudo que é relacionado ao linha de empate
app_linha = Label(frame_cima, text='', width=255, anchor='center', font='Ivy 1 bold', bg=co0, fg=co0)
app_linha.place(x=0, y=95)
# ----------------------------------------------------
# -- Label da Jogada dos jogadores
app_voce = Label(frame_baixo, text='', height=1, anchor='center', font='Ivy 10 bold', bg=co0, fg=co0)
app_voce.place(x=25, y=10)

app_pc = Label(frame_baixo, text='', height=1, anchor='center', font='Ivy 10 bold', bg=co0, fg=co0)
app_pc.place(x=190, y=10)
# ----------------------------------------------------
# -- Variaveis globais -------------------------------
# -- Aqui definimos os dois jogadores, 'Voce' e 'PC'

global voce         #-- Player 1
global pc           #-- Player 2
global rodadas      #-- Quantidade de rodadas
global pontos_voce  #-- Pontos do Player 1
global pontos_pc    #-- Pontos do Player 2

pontos_voce = 0     #-- Valor Inicial Player 1
pontos_pc = 0       #-- Valor Inicial Player 2
rodadas = 5         #-- Aqui define a quantidade de rodadas

# -- Função da lógica o Jogo -------------------------
# -- Nossa logica do jogo funciona da seguinte maneira:
# -- 1°. Controlar se a quantidade de rodadas esta excedida
# -- 2°. Caso esteja exedido tem que fazer alguma coisa
# -- 3° Ou terminar o jogo
# -- 4° Ou Decidir quem é o vencedor

def jogar(i):
    global rodadas
    global pontos_voce
    global pontos_pc

    if rodadas > 0:
        print(rodadas)
        opcoes = ['Pedra', 'Papel', 'Tesoura']
        pc = random.choice(opcoes)
        voce = i

        # -- Adiciona label da jogada do Player 01
        app_voce['text'] = pc
        app_voce['fg'] = 'white'

        # -- Adiciona label da jogada do Player 02
        app_pc['text'] = pc
        app_pc['fg'] = 'white'

        # -- Condição de Empate
        if voce == 'Pedra' and pc == 'Pedra':
            print('empate')
            app_1_linha['bg'] = co0     # -- Não Acende o linha de Ponto do Player 1
            app_2_linha['bg'] = co0     # -- Não Acende o linha de Ponto do Player 2
            app_linha['bg'] = co3       # -- Acende o linha de Empate

        elif voce == 'Papel' and pc == 'Papel':
            print('empate')
            app_1_linha['bg'] = co0     # -- Não Acende o linha de Ponto do Player 1
            app_2_linha['bg'] = co0     # -- Não Acende o linha de Ponto do Player 2
            app_linha['bg'] = co3       # -- Acende o linha de Empate

        elif voce == 'Tesoura' and pc == 'Tesoura':
            print('empate')
            app_1_linha['bg'] = co0     # -- Não Acende o linha de Ponto do Player 1
            app_2_linha['bg'] = co0     # -- Não Acende o linha de Ponto do Player 2
            app_linha['bg'] = co3       # -- Acende o linha de Empate

        # -- Condição de Pedra x Papel -- Movendo para frente
        elif voce == 'Pedra' and pc == 'Papel':
            print('Pc ganhou')
            app_1_linha['bg'] = co0     # -- Não Acende o linha de Ponto do Player 1
            app_2_linha['bg'] = co4     # -- Acende o linha de Ponto do Player 2
            app_linha['bg'] = co0       # -- Não Acende o linha de Empate

            pontos_pc += 10             # -- Adiciona 10 pontos

        # -- Condição de Pedra x Tesoura
        elif voce == 'Pedra' and pc == 'Tesoura':
            print('Voce ganhou')
            app_1_linha['bg'] = co4     # -- Acende o linha de Ponto do Player 1
            app_2_linha['bg'] = co0     # -- Não Acende o linha de Ponto do Player 2
            app_linha['bg'] = co0       # -- Não Acende o linha de Empate

            pontos_voce += 10           # -- Adiciona 10 pontos

        # -- Condição de Papel x Tesoura
        elif voce == 'Papel' and pc == 'Tesoura':
            print('Pc ganhou')
            app_1_linha['bg'] = co0     # -- Não Acende o linha de Ponto do Player 1
            app_2_linha['bg'] = co4     # -- Acende o linha de Ponto do Player 2
            app_linha['bg'] = co0       # -- Não Acende o linha de Empate

            pontos_pc += 10             # -- Adiciona 10 pontos

        # -- Condição de Pedra x Papel -- Movendo para tras
        elif voce == 'Papel' and pc == 'Pedra':
            print('Voce ganhou')
            app_1_linha['bg'] = co0     # -- Não Acende o linha de Ponto do Player 1
            app_2_linha['bg'] = co4     # -- Acende o linha de Ponto do Player 2
            app_linha['bg'] = co0       # -- Não Acende o linha de Empate

            pontos_voce += 10           # -- Adiciona 10 pontos

        # -- Condição de Pedra x Tesoura
        elif voce == 'Tesoura' and pc == 'Pedra':
            print('Pc ganhou')
            app_1_linha['bg'] = co0     # -- Não Acende o linha de Ponto do Player 1
            app_2_linha['bg'] = co4     # -- Acende o linha de Ponto do Player 2
            app_linha['bg'] = co0       # -- Não Acende o linha de Empate

            pontos_pc += 10             # -- Adiciona 10 pontos


        # -- Condição de Papel x Tesoura
        elif voce == 'Tesoura' and pc == 'Papel':
            print('Voce ganhou')
            app_1_linha['bg'] = co4     # -- Acende o linha de Ponto do Player 1
            app_2_linha['bg'] = co0     # -- Não Acende o linha de Ponto do Player 2
            app_linha['bg'] = co0       # -- Não Acende o linha de Empate

            pontos_voce += 10           # -- Adiciona 10 pontos'

        # -- Atualizaçãao da Pontuação
        app_1_pontos['text'] = pontos_voce  # -- Atualização da Pontuação do Player 01
        app_2_pontos['text'] = pontos_pc  # -- Atualização da Pontuação do Player 01

        # -- Atualizando o Numero de rodadas
        rodadas -= 1

    else:
        app_1_pontos['text'] = pontos_voce
        app_2_pontos['text'] = pontos_pc

        # -- Chama a função terminar o jogo
        fim_do_jogo()


# -- Função para iniciar o Jogo ----------------------
def iniciar_jogo():
    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3

    b_jogar.destroy()  # -- Elimina o Botão de Iniciar

    # -- Configurando o frame_baixo ----------------------
    # ------ Icone da Pedra
    icon_1 = Image.open('images/Hand_rock.png')
    icon_1 = icon_1.resize((50, 50), Image.Resampling.LANCZOS) # -- Image.ANTIALIAS
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon_1 = Button(frame_baixo, command=lambda: jogar('Pedra'),width=50, image=icon_1, compound=CENTER, bg=co0, fg=co0, font='Ivy 10 bold', anchor=CENTER, relief=FLAT)
    b_icon_1.place(x=15, y=60)

    # ------ Icone da Papel
    icon_2 = Image.open('images/Hand_paper.png')
    icon_2 = icon_2.resize((50, 50), Image.Resampling.LANCZOS) # -- Image.ANTIALIAS
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon_2 = Button(frame_baixo, width=50, command=lambda: jogar('Papel'),image=icon_2, compound=CENTER, bg=co0, fg=co0, font='Ivy 10 bold', anchor=CENTER, relief=FLAT)
    b_icon_2.place(x=95, y=60)

    #-------- Icone da tesoura
    icon_3 = Image.open('images/Hand_Scissors.png')
    icon_3 = icon_3.resize((50, 50), Image.Resampling.LANCZOS) # -- Image.ANTIALIAS
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon_3 = Button(frame_baixo, command=lambda: jogar('Tesoura'), width=50, image=icon_3, compound=CENTER, bg=co0, fg=co0, font='Ivy 10 bold', anchor=CENTER, relief=FLAT)
    b_icon_3.place(x=170, y=60)

# -- Função para terminar o Jogo ---------------------
def fim_do_jogo():
    global rodadas
    global pontos_voce
    global pontos_pc

    # -- Reiniciando as variaveis para Zero
    pontos_voce = 0                # -- Reinicia a pontuação do Player 1
    pontos_pc = 0                  # -- Reinicia a pontuação do Player 2
    rodadas = 5                    # -- Reinicia a pcontagem de rodadas
    # -- Definindo os Vencedores
    b_icon_1.destroy()             # -- Elimina o Botão 1
    b_icon_2.destroy()             # -- Elimina o Botão 2
    b_icon_3.destroy()             # -- Elimina o Botão 3

    # -- Definindo os Vencedores
    jogador_voce = int(app_1_pontos['text'])
    jogador_pc = int(app_2_pontos['text'])

    # -- Condições para os Vencedores
    if jogador_voce > jogador_pc:
        app_vencedor = Label(frame_baixo, text='Parabens, voce ganhou !!!', height=1, anchor='center', font='Ivy 10 bold', bg=co0, fg=co4)
        app_vencedor.place(x=5, y=60)
    elif jogador_voce < jogador_pc:
        app_vencedor = Label(frame_baixo, text='Infelizmente, voce perdeu !!!', height=1, anchor='center', font='Ivy 10 bold', bg=co0, fg=co5)
        app_vencedor.place(x=5, y=60)
    else:
        app_vencedor = Label(frame_baixo, text='Vocês Empataram !!!', height=1, anchor='center', font='Ivy 10 bold', bg=co0, fg=co3)
        app_vencedor.place(x=5, y=60)

    # -- Reiniciar o jogo

    def jogar_denovo():
        app_1_pontos['text'] = '0'        # -- Zera a contagem do Player 01
        app_1_pontos['text'] = '0'        # -- Zera a contagem do Player 01
        app_vencedor.destroy()            # -- Apaga o texto final

        b_jogar_denovo.destroy()          # -- Apaga o botão Jogar denovo

        iniciar_jogo()                    # -- Chama a função de iniciar o Jogo

    b_jogar_denovo = Button(frame_baixo, command=jogar_denovo, width=30, text='Jogar Denovo', compound=CENTER, bg=co5, fg='white',
    font='Ivy 10 bold', anchor=CENTER, relief=RAISED, overrelief=RIDGE)
    b_jogar_denovo.place(x=5, y=151)

#--------- Iniciar jogo
b_jogar = Button(frame_baixo, command=iniciar_jogo,  width=30, text='Jogar', compound=CENTER, bg=co5, fg='white', font='Ivy 10 bold', anchor=CENTER, relief=RAISED, overrelief=RIDGE)
b_jogar.place(x=5, y=151)
# ----------------------------------------------------

janela.mainloop()


