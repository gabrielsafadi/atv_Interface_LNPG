from tkinter import *
from tkinter import font
from tkinter.ttk import Combobox

arquivo = open('dados.txt', 'a')
arquivo.close()

def verificar():
  dados_cadastrados = cadastrados[tb.get()]
  lb_anolancamento.configure(text=f'Ano de Lançamento: {dados_cadastrados[0]}')
  lb_nomedabanda.configure(text=f'Nome da banda: {dados_cadastrados[1]}')
  lb_lancamento.configure(text=f'Álbum Lançamento: {dados_cadastrados[2]}')

def cadastrar_album():
  nome_album = txtalb.get()
  ano_album = txtano.get()
  nome_banda = txtband.get()
  lancamento = tb_tela1.get()

  arquivo = open('dados.txt', 'a')
  arquivo.write(f'{nome_album}%{ano_album}%{nome_banda}%{lancamento}\n')
  arquivo.close()

  window.destroy()
  tela_dados_salvos()

def tela_dados_salvos():
  global lb_lancamento, lb_nomedabanda, lb_anolancamento, cadastrados, tb

  ### Configuraçao da janela
  janela2 = Tk()
  janela2.title('Dados Salvos')
  janela2.geometry('500x500')

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
  Label(janela2, text='Álbuns Cadastrados', font='arial 14').place(x=180, y=50)
  tb = Combobox(janela2, value=nomes, font='arial 14')
  tb.place(x=25, y=125)

  ### butao
  Button(janela2, text='Verificar', font='arial 14', command=verificar).place(x=300, y=120)

  ### Ano de lancamento
  lb_anolancamento = Label(janela2, text='Ano de Lançamento: ', font='arial 14')
  lb_anolancamento.place(x=25, y=200)

  ### Nome da Banda 
  lb_nomedabanda = Label(janela2, text='Nome da Banda: ', font='arial 14')
  lb_nomedabanda.place(x=25, y=250)

  ## Lançamento
  lb_lancamento = Label(janela2, text='Álbum Lançamento: ', font='arial 14')
  lb_lancamento.place(x=25, y=300)

  janela2.mainloop()

window = Tk()
window.title('Albuns')
window.geometry('500x500')

### tela cadastro
lblalb = Label(window, text= 'Informações do Album', font='arial 14')
lblalb.place(x = 200, y = 50)

lblalb = Label(window, text= 'Nome do Album:', font='arial 14')
lblalb.place(x = 20, y = 175)
txtalb = Entry(window,  bd = 5, width=40)
txtalb.place(x = 20, y = 200)

lblano = Label(window, text= 'Ano do Album:', font='arial 14')
lblano.place(x = 20, y = 225)
txtano = Entry(window, bd = 5, width=40)
txtano.place(x = 20, y = 250)

lblband = Label(window, text= 'Nome da Banda/Artista:', font='arial 14')
lblband.place(x = 20, y = 275)
txtband = Entry(window, bd = 5, width=40)
txtband.place(x = 20, y = 300)

lblband = Label(window, text= 'Album lançamento?', font='arial 14')
lblband.place(x = 20, y = 350)

tb_tela1 = Combobox(window, values=['Sim', 'Nao'], font='arial 14')
tb_tela1.place(x=20, y=380)

botao_cadastro = Button(text="Cadatrar Álbum", font='arial 14', command=cadastrar_album)
botao_cadastro.place(x = 20, y = 420)


window.mainloop()