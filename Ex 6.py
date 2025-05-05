from tkinter import*

def salvar ():
with open ('estoque.txt', 'a') as arquivo:
arquivo.write(f'Medicamento:{entrada_medicamento.get()},'
f'Forma Farmacêutica:{entrada_forma.get()},'
f'Data de validade:{entrada_data.get()},'
f'Preço do produto: R${entrada_valor.get()},'
f'Quantidade em Estoque:{entrada_quantidade.get()},'
f'Número do lote: {entrada_lote.get()},'
f'Número de Telefone para contato: {entrada_contato.get()},'
f'Endereço do Fornecedor:{entrada_endereco.get()}\n')

def ler():
janela2 = Tk()
janela.config(padx=10, pady=10)
janela2.option_add('*Font', 'Verdana 12')
janela.title('Dados registrados')
lista_medicamentos = Label(janela2)
lista_medicamentos.grid(row=1, column=0, columnspan=8)

with open('estoque.txt','r') as arquivo:
linhas = arquivo.readlines()

conteudo = ''.join(linhas)
lista_medicamentos.config(text=conteudo)



janela = Tk()
janela.title('Controle de Estoque (Fármacia)')
janela.config(padx=10, pady=10)

quadro_registro = LabelFrame(janela, text= 'Drogasil', padx= 10, pady= 10, font='Verdana 12 italic',fg= 'red')
quadro_registro.grid(row=0, column=0, sticky= 'we')

medicamento = Label(quadro_registro, text= 'Medicamento:', anchor='e')
medicamento.grid(row=1, column=0, sticky='we')

entrada_medicamento = Entry(quadro_registro, width=40)
entrada_medicamento.grid(row=1,columnspan=2, column=1)

forma = Label(quadro_registro, text= 'Forma farmacêutica:', anchor='e')
forma.grid(row=1, column=3, sticky='we')

entrada_forma = Entry(quadro_registro, width=41)
entrada_forma.grid(row=1,columnspan=2, column=4)

data = Label(quadro_registro, text= 'Data de validade:', anchor='e')
data.grid(row=2, column=0, sticky='we')

entrada_data = Entry(quadro_registro, width=20)
entrada_data.grid(row=2,column=1)

valor = Label(quadro_registro, text= 'Preço do produto R$:', anchor='e')
valor.grid(row=2, column=2, sticky='we')

entrada_valor = Entry(quadro_registro, width=18)
entrada_valor.grid(row=2,column=3)

quantidade = Label(quadro_registro, text= 'Quantidade em estoque:', anchor='w')
quantidade.grid(row=2, column=4, sticky='we')

entrada_quantidade = Entry(quadro_registro, width=18)
entrada_quantidade.grid(row=2,column=5)

quadro_fornecedor = LabelFrame(janela, text= 'Dados do Fornecedor', padx= 10, pady= 10, font='Verdana 12 italic',fg= 'red')
quadro_fornecedor.grid(row=3, column=0, sticky= 'we')


lote = Label(quadro_fornecedor, text= 'Número do lote:', anchor='e')
lote.grid(row=3, column=0, sticky='we')

entrada_lote = Entry(quadro_fornecedor, width=35)
entrada_lote.grid(row=3, column=1)

contato = Label(quadro_fornecedor, text= 'Número de telefone para contato:', anchor='e')
contato.grid(row=3, column=2, sticky='we')

entrada_contato = Entry(quadro_fornecedor, width=35)
entrada_contato.grid(row=3, column=3)

endereco = Label(quadro_fornecedor, text= 'Endereço do Fornecedor:', anchor='e')
endereco.grid(row=4, column=0, sticky='we')

entrada_endereco = Entry(quadro_fornecedor, width=102)
entrada_endereco.grid(row=4,columnspan=3 , column=1)

quadro_botao = LabelFrame(janela, padx= 10, pady = 10, borderwidth=0)
quadro_botao.grid(row=5, column=0, sticky='we')

salvar = Button(quadro_botao, text= 'Salvar', anchor= 'w', command= salvar)
salvar.grid(row=6, column=0, sticky='w')

ler = Button(quadro_botao, text= 'Ler', anchor= 'w', command= ler)
ler.grid(row=6,column=1, sticky='we')


janela.mainloop()