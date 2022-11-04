# -- Importação da interface grafica ----------
import tkinter
from tkinter import *
from tkinter import ttk

# Importando o Pillow --------------------------
from PIL import Image, ImageTk

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
janela.title('')
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

# -- Configurando o frame_baixo ----------------------

# ------ Icone da Pedra
icon_1 = Image.open('images/Hand_rock.png')
icon_1 = icon_1.resize((50, 50), Image.Resampling.LANCZOS) # -- Image.ANTIALIAS
icon_1 = ImageTk.PhotoImage(icon_1)
b_icon_1 = Button(frame_baixo, width=50, image=icon_1, compound=CENTER, bg=co0, fg=co0, font='Ivy 10 bold', anchor=CENTER, relief=FLAT)
b_icon_1.place(x=15, y=60)

# ------ Icone da Papel
icon_2 = Image.open('images/Hand_paper.png')
icon_2 = icon_2.resize((50, 50), Image.Resampling.LANCZOS) # -- Image.ANTIALIAS
icon_2 = ImageTk.PhotoImage(icon_2)
b_icon_2 = Button(frame_baixo, width=50, image=icon_2, compound=CENTER, bg=co0, fg=co0, font='Ivy 10 bold', anchor=CENTER, relief=FLAT)
b_icon_2.place(x=95, y=60)

#-- ------ Icone da tesoura
#-- icon_3 = Image.open('images/Hand_Scissors.png')
#-- icon_3 = icon_3.resize((50, 50), Image.Resampling.LANCZOS) # -- Image.ANTIALIAS
#-- icon_3 = ImageTk.PhotoImage(icon_2)
#-- b_icon_3 = Button(frame_baixo, width=50, image=icon_3, compound=CENTER, bg=co0, fg=co0, font='Ivy 10 bold', anchor=CENTER, relief=FLAT)
#-- b_icon_3.place(x=170, y=60)


janela.mainloop()
