# Entrada

import sqlite3
from tkinter import *


def criar_banco():
    conexao = sqlite3.connect('cadastro.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dados_pessoais (
            CPF TEXT PRIMARY KEY,
            Nome TEXT,
            Telefone TEXT,
            Data_Nasc TEXT

        )
    ''')

    cursor.execute('''  
        CREATE TABLE IF NOT EXISTS enderecos_pessoais (
            id INTEGER PRIMARY KEY,
            Rua TEXT,
            Numero INTEGER,
            Bairro TEXT,
            Cidade TEXT, 
            UF TEXT

        )
    ''')
    conexao.commit()
    conexao.close()


def listar():
    global saida
    global saida1
    global cpf1_entrada
    conexao = sqlite3.connect('cadastro.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM dados_pessoais')
    dados_pessoais = cursor.fetchall()
    cursor.execute('SELECT * FROM enderecos_pessoais')
    enderecos_pessoais = cursor.fetchall()


    janela1 = Tk()
    janela1.title('Cadastro de alunos')
    janela1.config(padx=10, pady=10)

    quadro_dados2 = LabelFrame(janela1, text='', padx=10, pady=10, font='Verdana 12 italic', fg='red', borderwidth=0)
    quadro_dados2.grid(row=1, column=0, sticky='we')

    cpf1 = Label(quadro_dados2,text= 'CPF:', anchor='w')
    cpf1.grid(row=0, column=0, sticky='w')

    cpf1_entrada = Entry(quadro_dados2)
    cpf1_entrada.grid(row=0, column=1)

    botao_buscar = Button(quadro_dados2, text='Buscar', command=buscar)
    botao_buscar.grid(row=0, column=2)

    quadro_dados1 = LabelFrame(janela1, text='Dados Pessoais', padx=10, pady=10, font='Verdana 12 italic', fg='red')
    quadro_dados1.grid(row=2, column=0, sticky='we')

    saida = Label(quadro_dados1, text='', justify='left')
    saida.grid(row=3, column=0, columnspan=2)

    quadro_endereco = LabelFrame(janela1, text='Endereço', padx=10, pady=10, font='Verdana 12 italic', fg='red')
    quadro_endereco.grid(row=4, column=0, sticky='we')

    saida1 = Label(quadro_endereco, text='', justify='left')
    saida1.grid(row=5, column=0, columnspan=2)


    for i in dados_pessoais:
        saida['text'] += '\n' + str(i)

    for i in enderecos_pessoais:
        saida1['text'] += '\n' + str(i)

    conexao.close()



def salvar():
    conexao = sqlite3.connect('cadastro.db')
    cursor = conexao.cursor()
    cursor.execute(
        'INSERT INTO dados_pessoais (CPF, Nome, Telefone, Data_Nasc) VALUES (?,?,?,?)',
        (entrada_cpf.get(), entrada_nome.get(), entrada_telefone.get(), entrada_data.get()))
    cursor.execute(
        'INSERT INTO enderecos_pessoais (Rua, Numero, Bairro, Cidade, UF) VALUES (?,?,?,?,?)',
        (entrada_rua.get(), entrada_numero.get(), entrada_bairro.get(), entrada_cidade.get(), entrada_uf.get()))
    conexao.commit()
    conexao.close()



def buscar():
    global saida
    conexao = sqlite3.connect('cadastro.db')
    cursor = conexao.cursor()
    cursor.execute(f"SELECT * FROM dados_pessoais WHERE CPF = '{cpf1_entrada.get()}'")
    dados_pessoais = cursor.fetchall()

    saida['text'] = 'Leitura de dados:'
    if dados_pessoais:
        for dado_pessoal in dados_pessoais:
            saida['text'] += '\n' + str(dado_pessoal)
    else:
        saida['text'] += '\nNenhum dado encontrado para o CPF informado.'

    conexao.close()



janela = Tk()
janela.title('Cadastro')
janela.config(padx=10, pady=10)

quadro_dados = LabelFrame(janela, text='Dados Pessoais', padx=10, pady=10, font='Verdana 12 italic', fg='red')
quadro_dados.grid(row=0, column=0, sticky='we')

nome = Label(quadro_dados, text='Nome:', anchor='e')
nome.grid(row=1, column=0, sticky='we')

entrada_nome = Entry(quadro_dados, width=82)
entrada_nome.grid(row=1, columnspan=5, column=1)

cpf = Label(quadro_dados, text='CPF:', anchor='e')
cpf.grid(row=2, column=0, sticky='we')

entrada_cpf = Entry(quadro_dados)
entrada_cpf.grid(row=2, column=1)

telefone = Label(quadro_dados, text='Telefone:', anchor='e')
telefone.grid(row=2, column=2, sticky='we')

entrada_telefone = Entry(quadro_dados)
entrada_telefone.grid(row=2, column=3)

data = Label(quadro_dados, text='Data Nasc:', anchor='e')
data.grid(row=2, column=4, sticky='we')

entrada_data = Entry(quadro_dados)
entrada_data.grid(row=2, column=5)

quadro_endereco = LabelFrame(janela, text='Endereço', padx=10, pady=10, font='Verdana 12 italic', fg='red')
quadro_endereco.grid(row=3, column=0, sticky='we')

rua = Label(quadro_endereco, text='Rua:', anchor='e')
rua.grid(row=4, column=0, sticky='we')

entrada_rua = Entry(quadro_endereco, width=69)
entrada_rua.grid(row=4, columnspan=3, column=1)

numero = Label(quadro_endereco, text='N°:', anchor='e')
numero.grid(row=4, column=4, sticky='we')

entrada_numero = Entry(quadro_endereco, width=9)
entrada_numero.grid(row=4, column=5)

bairro = Label(quadro_endereco, text='Bairro:', anchor='e')
bairro.grid(row=5, column=0, sticky='we')

entrada_bairro = Entry(quadro_endereco, width=30)
entrada_bairro.grid(row=5, column=1)

cidade = Label(quadro_endereco, text='Cidade:', anchor='e')
cidade.grid(row=5, column=2, sticky='we')

entrada_cidade = Entry(quadro_endereco, width=30)
entrada_cidade.grid(row=5, column=3)

uf = Label(quadro_endereco, text='UF:', anchor='e')
uf.grid(row=5, column=4, sticky='we')

entrada_uf = Entry(quadro_endereco, width=9)
entrada_uf.grid(row=5, column=5)

quadro_botao = LabelFrame(janela, padx=10, pady=10, borderwidth=0)
quadro_botao.grid(row=6, column=0, sticky='we')

dados = Button(quadro_botao, text='Gravar dados', anchor='w', command=salvar)
dados.grid(row=7, column=0, sticky='w')

botao_lista = Button(quadro_botao, text='Listar', anchor='w', command=listar)
botao_lista.grid(row=7, column=1, sticky='we')



janela.mainloop()
criar_banco()
listar()