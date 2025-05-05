from tkinter import *
import emoji

def salvar():
    with open('estoques.txt', 'a') as arquivo:
        arquivo.write(f'Medicamento:{entrada_medicamento.get()},'
                      f'Forma Farmacêutica:{entrada_forma.get()},'
                      f'Data de validade:{entrada_data.get()},'
                      f'Preço do produto: R${entrada_valor.get()},'
                      f'Quantidade em Estoque:{entrada_quantidade.get()},\n'
                      f'Número do lote: {entrada_lote.get()},'
                      f'Número de Telefone para contato: {entrada_contato.get()},'
                      f'Endereço do Fornecedor:{entrada_endereco.get()}\n\n')
        entrada_medicamento.delete(0, END)
        entrada_forma.delete(0, END)
        entrada_data.delete(0, END)
        entrada_valor.delete(0, END)
        entrada_quantidade.delete(0, END)
        entrada_lote.delete(0, END)
        entrada_contato.delete(0, END)
        entrada_endereco.delete(0, END)


def ler():
    global janela2
    janela2 = Tk()
    janela.config(padx=10, pady=10)
    janela2.option_add('*Font', 'Verdana 12')
    janela.title('Dados registrados')

    lista_medicamentos = Label(janela2)
    lista_medicamentos.grid(row=1, column=0, columnspan=8)

    botao_voltar = Button(janela2, text='Voltar', command=voltar)
    botao_voltar.grid(row=2, column=0)

    with open('estoques.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

        conteudo = ''.join(linhas)
        lista_medicamentos.config(text=conteudo)

        janela.destroy()


def voltar():
    janela2.destroy()
    abrir_janela()


def abrir_janela():
    global entrada_medicamento, entrada_forma, entrada_data, entrada_valor, entrada_quantidade, entrada_lote, entrada_contato, entrada_endereco, janela

    janela = Tk()
    janela.title('Controle de Estoque (Fármacia)')
    janela.config(padx=10, pady=10)

    quadro_registro = LabelFrame(janela, text= emoji.emojize(':ambulance: Farmacia Hospitalar'), padx=10, pady=10, font='Verdana 12 italic', fg='red')
    quadro_registro.grid(row=0, column=0, sticky='we')

    medicamento = Label(quadro_registro, text='Medicamento:', anchor='e')
    medicamento.grid(row=1, column=0, sticky='we')

    entrada_medicamento = Entry(quadro_registro, width=40)
    entrada_medicamento.grid(row=1, columnspan=2, column=1)

    forma = Label(quadro_registro, text='Forma farmacêutica:', anchor='e')
    forma.grid(row=1, column=3, sticky='we')

    entrada_forma = Entry(quadro_registro, width=41)
    entrada_forma.grid(row=1, columnspan=2, column=4)

    data = Label(quadro_registro, text='Data de validade:', anchor='e')
    data.grid(row=2, column=0, sticky='we')

    entrada_data = Entry(quadro_registro, width=20)
    entrada_data.grid(row=2, column=1)

    valor = Label(quadro_registro, text='Preço do produto R$:', anchor='e')
    valor.grid(row=2, column=2, sticky='we')

    entrada_valor = Entry(quadro_registro, width=18)
    entrada_valor.grid(row=2, column=3)

    quantidade = Label(quadro_registro, text='Quantidade em estoque:', anchor='w')
    quantidade.grid(row=2, column=4, sticky='we')

    entrada_quantidade = Entry(quadro_registro, width=18)
    entrada_quantidade.grid(row=2, column=5)

    quadro_fornecedor = LabelFrame(janela, text='Dados do Fornecedor', padx=10, pady=10, font='Verdana 12 italic',
                                   fg='red')
    quadro_fornecedor.grid(row=3, column=0, sticky='we')

    lote = Label(quadro_fornecedor, text='Número do lote:', anchor='e')
    lote.grid(row=3, column=0, sticky='we')

    entrada_lote = Entry(quadro_fornecedor, width=31)
    entrada_lote.grid(row=3, column=1)

    contato = Label(quadro_fornecedor, text='Número de telefone para contato:', anchor='e')
    contato.grid(row=3, column=2, sticky='we')

    entrada_contato = Entry(quadro_fornecedor, width=31)
    entrada_contato.grid(row=3, column=3)

    endereco = Label(quadro_fornecedor, text='Endereço do Fornecedor:', anchor='e')
    endereco.grid(row=4, column=0, sticky='we')

    entrada_endereco = Entry(quadro_fornecedor, width=94)
    entrada_endereco.grid(row=4, columnspan=3, column=1)

    quadro_botao = LabelFrame(janela, padx=10, pady=10, borderwidth=0)
    quadro_botao.grid(row=5, column=0, sticky='we')

    botao_salvar = Button(quadro_botao, text='Salvar', anchor='w', command=salvar)
    botao_salvar.grid(row=6, column=0, sticky='w')

    botao_ler = Button(quadro_botao, text='Ler', anchor='w', command=ler)
    botao_ler.grid(row=6, column=1, sticky='we')

    janela.mainloop()


abrir_janela()