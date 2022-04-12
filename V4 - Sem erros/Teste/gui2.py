from tkinter import *
from tkinter.ttk import Combobox
from domain2 import banda


def tela_cadastro():
    teste = banda()
    global txtalb, txtano, txtband, opcaoLancamento, telaCadastro
    telaCadastro = Toplevel()
    telaCadastro.title('Trabalho de LNPG')
    telaCadastro.geometry('500x500')
    telaCadastro.resizable(False, False)
    bg = PhotoImage(file='bg.png')
    Label(telaCadastro, image=bg).pack()

    ### tela cadastro
    Label(telaCadastro, text= 'Informações do Álbum', font='arial 18', fg='#32cd32', bg='#121212').place(x = 130, y = 50)

    Label(telaCadastro, text= 'Nome do Álbum:', font='arial 15', fg='whitesmoke', bg='#121212').place(x = 50, y = 100)
    txtalb = Entry(telaCadastro,  width=22, font='arial 13', bg='#272727', bd=0, fg='whitesmoke')
    txtalb.place(x = 50, y = 130)

    Label(telaCadastro, text='Ano do Álbum:', font='arial 15', fg='whitesmoke', bg='#121212').place(x = 50, y = 170)
    txtano = Entry(telaCadastro, width=22, font='arial 13', bg='#272727', bd=0, fg='whitesmoke')
    txtano.place(x = 50, y = 200)

    Label(telaCadastro, text= 'Nome da Banda/Artista:', font='arial 15', fg='whitesmoke', bg='#121212').place(x = 50, y = 240)
    txtband = Entry(telaCadastro, width=22, font='arial 13', bg='#272727', bd=0, fg='whitesmoke')
    txtband.place(x = 50, y = 270)

    Label(telaCadastro, text= 'Álbum lançamento?', font='arial 15', fg='whitesmoke', bg='#121212').place(x = 50, y = 310)

    opcaoLancamento = IntVar()
    op_sim = Radiobutton(
      telaCadastro, value=1, variable=opcaoLancamento,
      font='arial 13', bg='#121212', fg='#32cd32', text='Sim',
      activebackground='#121212', activeforeground='whitesmoke', selectcolor='#272727'
    )
    op_sim.place(x=50, y=340)

    op_nao = Radiobutton(
      telaCadastro, value=2, variable=opcaoLancamento, 
      font='arial 13', bg='#121212', fg='#32cd32', text='Nao',
      activebackground='#121212', activeforeground='whitesmoke', selectcolor='#272727'
    )
    op_nao.place(x=150, y=340)

    Button(telaCadastro, text="Cadatrar Álbum", font='arial 15', command=teste.cadastrar_album(txtalb, txtano, txtband, opcaoLancamento), bg='#32cd32', fg='white').place(x = 170, y = 400)


    telaCadastro.destroy()
    telaCadastro.mainloop()
tela_cadastro()