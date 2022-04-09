from tkinter import *
from tkinter.ttk import Combobox

def solicitar():
    fatorDeBusca = busca.get()

    arquivo = open('dados.txt', 'r')
    dados = arquivo.readlines()
    nome_do_artista = []
    cadastrados = {}
    for album in dados:
        album = album.split('%')
        nome_do_artista.append(album[2])
        cadastrados.setdefault(album[2], [album[0], album[1], album[3]])
    arquivo.close()

    print(cadastrados)

    albuns_achados = []
    for nome in nome_do_artista:
        print(fatorDeBusca in nome)
        print(nome)
        if fatorDeBusca in nome:
            albuns_achados.append(cadastrados[nome][0])

    print(albuns_achados)

    tb_dados.configure(values=albuns_achados)



janela = Tk()
janela.geometry('500x500')

Label(janela, text='Buscar por band/artista').pack()
busca = Entry(janela, bd=5)
busca.pack()


tb_dados = Combobox(janela)
tb_dados.pack()

Button(janela, text='Buscar', command=solicitar).pack()


janela.mainloop()
