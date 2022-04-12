from db import *

class banda:
    def cadastrar_album(album, ano, banda, lancamento):
        consulta = database()

        if lancamento == 1:
            consulta.gravar_dados(f'{album}%{ano}%{banda}%Sim\n')
        else:
            consulta.gravar_dados(f'{album}%{ano}%{banda}%Nao\n')