from tkinter import *
from tkinter.ttk import Combobox

arquivo = open('dados.txt', 'a')
arquivo.close()

def verificar():
  dados_cadastrados = cadastrados[tb.get()]
  lb_anolancamento.configure(text=f'Ano de Lançamento: {dados_cadastrados[0]}')
  lb_nomedabanda.configure(text=f'Nome da Banda: {dados_cadastrados[1]}')
  lb_lancamento.configure(text=f'Álbum Lançamento: {dados_cadastrados[2]}')

def cadastrar_album():
  nome_album = txtalb.get()
  ano_album = txtano.get()
  nome_banda = txtband.get()
  lancamento = opcaoLancamento.get()

  arquivo = open('dados.txt', 'a')
  if lancamento == 1:
    arquivo.write(f'{nome_album}%{ano_album}%{nome_banda}%Sim\n')
  else:
    arquivo.write(f'{nome_album}%{ano_album}%{nome_banda}%Nao\n')
  arquivo.close()

  telaCadastro.destroy()
  tela_dados_salvos()

def tela_dados_salvos():
  global lb_lancamento, lb_nomedabanda, lb_anolancamento, cadastrados, tb

  ### Configuraçao da janela
  telaDadosSalvos = Tk()
  telaDadosSalvos.title('Dados Salvos')
  telaDadosSalvos.geometry('500x500')
  bg = PhotoImage(file='bg.png')
  Label(telaDadosSalvos, image=bg).pack()

  ### Lendo e agrupando dados 
  arquivo = open('dados.txt', 'r')
  dados = arquivo.readlines()
  nomes = []
  cadastrados = {}
  for album in dados:
      album = album.split('%')
      nomes.append(album[0])
      cadastrados.setdefault(album[0], album[1:])
  arquivo.close()

  ### Lista de Dados na Interface
  Label(telaDadosSalvos, text='Álbuns Cadastrados', font='arial 18', fg='#32cd32', bg='#121212').place(x=140, y=50)
  tb = Combobox(telaDadosSalvos, value=nomes, font='arial 14')
  tb.place(x=80, y=125)

  ### butao
  Button(telaDadosSalvos, text='Verificar', font='arial 12', command=verificar, bg='#32cd32', fg='white').place(x=330, y=125)

  ### Ano de lancamento
  lb_anolancamento = Label(telaDadosSalvos, text='Ano de Lançamento: ', font='arial 14', fg='white', bg='#121212')
  lb_anolancamento.place(x=55, y=200)

  ### Nome da Banda 
  lb_nomedabanda = Label(telaDadosSalvos, text='Nome da Banda: ', font='arial 14', fg='white', bg='#121212')
  lb_nomedabanda.place(x=55, y=250)

  ## Lançamento
  lb_lancamento = Label(telaDadosSalvos, text='Álbum Lançamento: ', font='arial 14', fg='white', bg='#121212')
  lb_lancamento.place(x=55, y=300)

  telaDadosSalvos.mainloop()

def tela_cadastro():
  global txtalb, txtano, txtband, opcaoLancamento, telaCadastro
  telaCadastro = Tk()
  telaCadastro.title('Albuns')
  telaCadastro.geometry('500x500')
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
    activebackground='#121212', activeforeground='#32cd32'
  )
  op_sim.place(x=50, y=340)

  op_nao = Radiobutton(
    telaCadastro, value=2, variable=opcaoLancamento, 
    font='arial 13', bg='#121212', fg='#32cd32', text='Nao',
    activebackground='#121212', activeforeground='#32cd32'
  )
  op_nao.place(x=150, y=340)

  Button(text="Cadatrar Álbum", font='arial 15', command=cadastrar_album, bg='#32cd32', fg='white').place(x = 170, y = 400)

  telaCadastro.mainloop()

tela_cadastro()
