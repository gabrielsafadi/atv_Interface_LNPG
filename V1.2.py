from tkinter import *



window = Tk()
window.title('Albuns')
window.geometry("500x500")

lista_albuns = []

def cadastrar_album():
  nome_album = txtalb.get()
  ano_album = txtano.get()
  nome_banda = txtband.get()
  lista_albuns.append((nome_album, ano_album, nome_banda))

lblalb = Label(window, text= 'Informações do Album')
lblalb.place(x = 200, y = 50)

lblalb = Label(window, text= 'Nome do Album')
lblalb.place(x = 20, y = 175)
txtalb = Entry(window, text = 'Nome do Album', bd = 5)
txtalb.place(x = 20, y = 200)

lblano = Label(window, text= 'Ano do Album')
lblano.place(x = 20, y = 225)
txtano = Entry(window, text = 'Ano do Album', bd = 5)
txtano.place(x = 20, y = 250)

lblband = Label(window, text= 'Nome da Banda/Artista')
lblband.place(x = 20, y = 275)
txtband = Entry(window, text = 'Nome da Banda', bd = 5)
txtband.place(x = 20, y = 300)

lblband = Label(window, text= 'Album lançamento?')
lblband.place(x = 20, y = 350)

v0=IntVar()
v0.set(1)
r1=Radiobutton(window, text="Sim", variable=v0, value=1)
r2=Radiobutton(window, text="Não", variable=v0, value=2)
r1.place(x=20,y=380)
r2.place(x=80, y=380)

botao_cadastro = Button(text="Cadatrar Álbum", command=cadastrar_album)
botao_cadastro.place(x = 20, y = 420)


window.mainloop() 

print(lista_albuns)