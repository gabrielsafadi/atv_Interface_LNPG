
class database:
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