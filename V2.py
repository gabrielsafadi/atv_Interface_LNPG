from tkinter import *
from tkinter.ttk import Combobox

arquivo = open('dados.txt', 'a')
arquivo.close()

### Banco de Dados
def buscar_dados():
  arquivo = open('dados.txt', 'r')
  dados = arquivo.readlines()
  albuns = []
  arquivo.close()
  for album in dados:
    album = album.split('%')
    albuns.append(album)
  return albuns

### Banco de Dados
def gravar_dados(texto):
  arquivo = open('dados.txt', 'a')
  arquivo.write(texto)
  arquivo.close()

### Regra de Negócio
def verificar_album():
  dados_cadastrados = cadastrados[tb.get()]
  lb_anolancamento.configure(text=f'Ano de Lançamento: {dados_cadastrados[0]}')
  lb_nomedabanda.configure(text=f'Nome da Banda: {dados_cadastrados[1]}')
  lb_lancamento.configure(text=f'Álbum Lançamento: {dados_cadastrados[2]}')

### 
def coletar_albuns_cadastrados():
  data = buscar_dados()
  nomes = []
  cadastrados = {}
  for album in data:
    nomes.append(album[0])
    cadastrados.setdefault(album[0], album[1:])
  return [nomes, cadastrados]

### Regra de Negócio
def cadastrar_album():
  nome_album = txtalb.get()
  ano_album = txtano.get()
  nome_banda = txtband.get()
  lancamento = opcaoLancamento.get()

  if lancamento == 1:
    gravar_dados(f'{nome_album}%{ano_album}%{nome_banda}%Sim\n')
  else:
    gravar_dados(f'{nome_album}%{ano_album}%{nome_banda}%Nao\n')

  telaCadastro.destroy()

### Regra de Negócio
def busca_por_artista():
    fatorDeBusca = busca.get().lower()
    coletados = ''
    for album in buscar_dados():
      nomeArtista = album[2].lower()
      if fatorDeBusca in nomeArtista:
          coletados += f'{album[0]} / {album[1]} / {album[2]}\n'

    resultadoDaBuscaArtista.configure(text=coletados)

### Regra de Negócio
def busca_por_ano():
    select = opcao.get()
    data = int(tb_Data.get())
    albuns_filtrados = ''

    if select == 1:
        for album in buscar_dados():
            if int(album[1]) < data:
                albuns_filtrados += f'{album[0]} / {album[1]} / {album[2]}\n'
    elif select == 2:
        for album in buscar_dados():
            if int(album[1]) > data:
                albuns_filtrados += f'{album[0]} / {album[1]} / {album[2]}\n'
    else:
        for album in buscar_dados():
            if int(album[1]) == data:
                albuns_filtrados += f'{album[0]} / {album[1]} / {album[2]}\n'

    
    resultadoDaBuscaAno.configure(text=albuns_filtrados)

### GUI
def tela_dados_salvos():
  global lb_lancamento, lb_nomedabanda, lb_anolancamento, cadastrados, tb

  ### Configuraçao da janela
  telaDadosSalvos = Toplevel()
  telaDadosSalvos.title('Trabalho de LNPG')
  telaDadosSalvos.geometry('500x500')
  telaDadosSalvos.resizable(False, False)
  bg = PhotoImage(file='bg.png')
  Label(telaDadosSalvos, image=bg).pack()

  ### Agrupando Dados para Interface
  data = coletar_albuns_cadastrados()
  nomes = data[0]
  cadastrados = data[1]
  

  ### Lista de Dados na Interface
  Label(telaDadosSalvos, text='Álbuns Cadastrados', font='arial 18', fg='#32cd32', bg='#121212').place(x=140, y=50)
  tb = Combobox(telaDadosSalvos, value=nomes, font='arial 14')
  tb.place(x=80, y=125)

  ### Botão
  Button(telaDadosSalvos, text='Verificar', font='arial 12', command=verificar_album, bg='#32cd32', fg='white').place(x=330, y=125)

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

### GUI
def tela_cadastro():
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

  Button(telaCadastro, text="Cadatrar Álbum", font='arial 15', command=cadastrar_album, bg='#32cd32', fg='white').place(x = 170, y = 400)

  telaCadastro.mainloop()

### GUI
def tela_busca_por_artista():
    global busca, resultadoDaBuscaArtista

    telaBuscaArtista = Toplevel()
    telaBuscaArtista.geometry('500x500')
    telaBuscaArtista.resizable(False, False)
    telaBuscaArtista.title('Trabalho de LNPG')
    bg = PhotoImage(file='bg.png')
    Label(telaBuscaArtista, image=bg).pack()

    Label(telaBuscaArtista, text='Buscar por Artista', font='arial 18', fg='#32cd32', bg='#121212').place(x=150, y=45)
    busca = Entry(telaBuscaArtista, font='arial 14', bg='#272727', fg='whitesmoke', bd=0,)
    busca.place(x=90, y=95, height=40)

    Button(telaBuscaArtista, text='Buscar', command=busca_por_artista, font='arial 16', bg='#32cd32', fg='white').place(x=320, y=95)
    Label(telaBuscaArtista, text='ÁLBUM /// ANO-DE-LANÇAMENTO /// ARTISTA', font='arial 13', fg='#32cd32', bg='#121212').place(x=60,y=160)

    resultadoDaBuscaArtista = Label(telaBuscaArtista, font='arial 12', text='', justify='left', fg='whitesmoke', bg='#121212')
    resultadoDaBuscaArtista.place(x=60, y=210)

    telaBuscaArtista.mainloop()

### GUI
def tela_busca_por_ano():
    global opcao, tb_Data, resultadoDaBuscaAno

    telaBuscaAno = Toplevel()
    telaBuscaAno.geometry('500x500')
    telaBuscaAno.resizable(False, False)
    telaBuscaAno.title('Trabalho de LNPG')
    bg = PhotoImage(file='bg.png')
    Label(telaBuscaAno, image=bg).pack()

    Label(telaBuscaAno, text='Buscar por Ano', font='arial 18', fg='#32cd32', bg='#121212').place(x=170, y=40)

    opcao = IntVar()
    op1 = Radiobutton(
        telaBuscaAno, text='Anterior a', value=1, variable=opcao,
        font='arial 13', bg='#121212', fg='#32cd32',
        activebackground='#121212', activeforeground='whitesmoke', selectcolor='#272727'
    )
    op1.place(x=60,y=100)

    op2 = Radiobutton(
        telaBuscaAno, text='Posterior a', value=2, variable=opcao,
        font='arial 13', bg='#121212', fg='#32cd32',
        activebackground='#121212', activeforeground='whitesmoke', selectcolor='#272727'
    )
    op2.place(x=170,y=100)

    op3 = Radiobutton(
        telaBuscaAno, text='Igual a', value=3, variable=opcao, 
        font='arial 13', bg='#121212', fg='#32cd32',
        activebackground='#121212', activeforeground='whitesmoke', selectcolor='#272727'
    )
    op3.place(x=290,y=100)

    tb_Data = Combobox(telaBuscaAno, values=[1980, 1990, 2000, 2010], font='arial 14', width=20)
    tb_Data.place(x=60, y=140)


    Button(telaBuscaAno, command=busca_por_ano, text='BUSCAR', font='arial 13', fg='white', bg='#32cd32').place(x=320, y=135)

    Label(telaBuscaAno, text='ÁLBUM /// ANO-DE-LANÇAMENTO /// ARTISTA', font='arial 13', fg='#32cd32', bg='#121212').place(x=60,y=185)

    resultadoDaBuscaAno = Label(telaBuscaAno, text='', font='arial 14', bg='#121212', fg='whitesmoke', justify='left')
    resultadoDaBuscaAno.place(x=60,y=220)

    telaBuscaAno.mainloop()

### GUI
def criarTelaInicial():
  telaInicial = Tk()
  telaInicial.geometry('500x500')
  telaInicial.title('Trabalho de LNPG')
  telaInicial.resizable(False, False)
  bg = PhotoImage(file='bg.png')
  Label(telaInicial, image=bg).pack()
  
  Button(telaInicial, text='Cadastrar Álbuns', command=tela_cadastro, fg='white', font='arial 20', bg='#32cd32', width=20).place(x=90, y=80)
  Button(telaInicial, text='Verificar Álbuns', command=tela_dados_salvos, fg='white', font='arial 20', bg='#272727', width=20).place(x=90, y=160)
  Button(telaInicial, text='Buscar por Artista', command=tela_busca_por_artista, fg='white', font='arial 20', bg='#272727', width=20).place(x=90, y=240)
  Button(telaInicial, text='Buscar por Data', command=tela_busca_por_ano, fg='white', font='arial 20', bg='#272727', width=20).place(x=90, y=320)

  telaInicial.mainloop()

criarTelaInicial()