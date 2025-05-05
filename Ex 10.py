from tkinter import*

def salvar():
    with open ('agenda.txt','a') as arquivo:
        arquivo.write(f'Nome:{entrada_nome.get()},'
                      f'Sobrenome: {entrada_sobrenome.get()}, '
                      f'Telefone: {entrada_telefone.get()}, '
                      f'Celular:{entrada_celular.get()} ,'
                      f'Email:{entrada_email.get()} ,'
                      f'Web:{entrada_web.get()}\n')

def ler():
    janela2 = Tk()
    janela.config(padx=10, pady=10)
    janela2.option_add('*Font', 'Verdana 12')
    janela.title('Dados cadastrados')
    lista_agenda = Label(janela2)
    lista_agenda.grid(row=1, column=0, columnspan=6)

    with open('agenda.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

        conteudo= ''.join(linhas)
        lista_agenda.config(text=conteudo)


janela =Tk()
janela.title('Agenda de Contatos')
janela.config(padx=10, pady= 10)

quadro_informacao = LabelFrame(janela, text= 'Inicio', padx= 10, pady= 10, font='Verdana 12 italic',fg= 'red')
quadro_informacao.grid(row=0, column=0, sticky= 'we')

nome = Label(quadro_informacao, text= 'Nome:', anchor='e')
nome.grid(row=1, column=0, sticky='we')

entrada_nome = Entry(quadro_informacao, width=50)
entrada_nome.grid(row=1,columnspan=3, column=1)

sobrenome = Label(quadro_informacao, text= 'Sobrenome:', anchor='e')
sobrenome.grid(row=2, column=0, sticky='we')

entrada_sobrenome = Entry(quadro_informacao, width=50)
entrada_sobrenome.grid(row=2,columnspan=3, column=1)

quadro_few = LabelFrame(janela, text= 'Celular/ Email / Web ', padx= 10, pady= 10, font='Verdana 9 italic',fg= 'black')
quadro_few.grid(row=3,column=0,sticky='we')

telefone = Label(quadro_few, text= 'Telefone:', anchor= 'e')
telefone.grid(row=4, column=0, sticky='we')

entrada_telefone = Entry(quadro_few, width=20)
entrada_telefone.grid(row=4,columnspan=1, column=1)

celular = Label(quadro_few, text= 'Celular:', anchor= 'e')
celular.grid(row=4, column=2, sticky='we')

entrada_celular = Entry(quadro_few, width=22)
entrada_celular.grid(row=4,columnspan=1, column=3)

email = Label(quadro_few, text= 'Email:', anchor= 'e')
email.grid(row=6, column=0, sticky='we')

entrada_email = Entry(quadro_few, width=50)
entrada_email.grid(row=6,columnspan=3, column=1)

web = Label(quadro_few, text= 'Web:', anchor= 'e')
web.grid(row=7, column=0, sticky='we')

entrada_web = Entry(quadro_few, width=50)
entrada_web.grid(row=7,columnspan=3, column=1)

quadro_botao = LabelFrame(janela, padx= 10, pady = 10, borderwidth=0)
quadro_botao.grid(row=8, column=0, sticky='we')

salvar = Button(quadro_botao, text= 'Salvar',  anchor= 'w', command= salvar)
salvar.grid(row=8, column=0, sticky='w')

ler = Button(quadro_botao, text= 'Ler',  anchor= 'w', command= ler)
ler.grid(row=8,column=1, sticky='we')

janela.mainloop()