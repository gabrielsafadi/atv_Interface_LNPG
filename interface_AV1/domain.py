from db import database


class banda:
    ### Regra de Negócio
    def verificar_album():
    dados_cadastrados = cadastrados[tb.get()]
    lb_anolancamento.configure(text=f'Ano de Lançamento: {dados_cadastrados[0]}')
    lb_nomedabanda.configure(text=f'Nome da Banda: {dados_cadastrados[1]}')
    lb_lancamento.configure(text=f'Álbum Lançamento: {dados_cadastrados[2]}')

    ### Regra de Negócio
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

