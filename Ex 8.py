from tkinter import ttk
from tkinter import *
import sqlite3
import datetime
import emoji
from tkinter import messagebox
from ttkthemes import ThemedStyle


def criar_banco():
    conexao = sqlite3.connect('farmacia.db')
    cursor = conexao.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS data_farmacia (
    id INTEGER PRIMARY KEY,
    Medicamento TEXT,
    Data_Validade TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS banco_farmacia (
     id INTEGER PRIMARY KEY,
     Medicamento TEXT,
     Medida TEXT,
     Forma_Farmaceutica TEXT,
     Quantidade TEXT
    )
    ''')
    conexao.commit()
    conexao.close()

def salvar():

    quantidade = quantidade1.get()

    if not quantidade.isdigit():
        mensagem = Label(quadrobotao, text='Só é permitido números, no campo de quantidade!.', pady=5,
                         padx=5, font='Verdana 16 italic', fg='red')
        mensagem.grid(row=6, column=3)
        return

    else:
        mensagem = Label(quadrobotao, text='Informações salvas com sucesso!', pady=5, padx=5, font='Verdana 14 italic')
    mensagem.grid(row=6, column=2)

    cont = len(medicamento1.get())
    cont1 = len(data_de_validade1.get())
    cont2 = len(medida1.get())
    cont3 = len(forma_farmaceutica1.get())
    cont4 = len(quantidade1.get())

    if cont > 0 and cont1 > 0 and cont2 > 0 and cont3 > 0 and cont4 > 0:

        conexao = sqlite3.connect('farmacia.db')
        cursor = conexao.cursor()
        cursor.execute(
            'INSERT INTO data_farmacia (Medicamento, Data_Validade) VALUES (?,?)',
            (medicamento1.get(), data_de_validade1.get()))
        cursor.execute(
            'INSERT INTO banco_farmacia (Medicamento, Medida, Forma_Farmaceutica, Quantidade) VALUES (?,?,?,?)',
            (medicamento1.get(), medida1.get(), forma_farmaceutica1.get(), quantidade1.get())
        )

        conexao.commit()

        conexao.close()

        medicamento1.delete(0, END)
        medida1.delete(0, END)
        forma_farmaceutica1.delete(0, END)
        quantidade1.delete(0, END)
        data_de_validade1.delete(0, END)

    else:
        messagebox.showwarning('Cuidado', 'Não preencheu todas os campos corretamente!')

def avancar():

    def editar_quantidade():
        item_selecionado = table_banco.selection()
        if item_selecionado:
            item_id = table_banco.item(item_selecionado)['values'][0]  # Extrai o ID do item selecionado
            quantidade_atual = table_banco.item(item_selecionado)['values'][4]  # Extrai a quantidade atual
            janela_edicao = Tk()
            janela_edicao.title("Editar Quantidade")
            janela_edicao.config(borderwidth=20, bg='pink')

            nova_quantidade_label = Label(janela_edicao, fg='purple', bg='pink', font='Verdana 10 italic', text=emoji.emojize('\u27F3 Nova Quantidade'))
            nova_quantidade_label.grid(row=0, column=0)
            nova_quantidade_entry = Entry(janela_edicao)
            nova_quantidade_entry.grid(row=1, column=0, sticky='we')

            salvar_edicao_button = Button(janela_edicao,fg='purple', text="Salvar", command=lambda: salvar_edicao(item_selecionado, nova_quantidade_entry.get()))
            salvar_edicao_button.grid()

            janela_edicao.mainloop()
        else:
            messagebox.showinfo("Aviso", "Nenhum item selecionado.")

    def salvar_edicao(item_selecionado, nova_quantidade):
        table_banco.set(item_selecionado, column='Quantidade', value=nova_quantidade)
        item_id = table_banco.item(item_selecionado)['values'][0]  # Extrai o ID do item selecionado
        atualizar_quantidade_banco(item_id, nova_quantidade)

    def atualizar_quantidade_banco(item_id, nova_quantidade):
        conexao = sqlite3.connect('farmacia.db')
        cursor = conexao.cursor()
        cursor.execute("UPDATE banco_farmacia SET Quantidade=? WHERE id=?", (nova_quantidade, item_id))
        conexao.commit()
        conexao.close()

    global table_validade, table_banco

    janela2 = Tk()
    janela2.title("")
    janela2.config(borderwidth=30)

    quadro_validade = LabelFrame(janela2, bg='pink', font='Verdana 12 italic', fg='black', text=emoji.emojize(':calendar: Data de Validade e Vencimento'), padx=10, pady=10)
    quadro_validade.grid(row=0, column=0, sticky='we')

    quadro_banco = LabelFrame(janela2, bg='pink', font='verdana 12 italic', fg='black', text=emoji.emojize(':package: Banco de Dados e Armazenamento'), padx=10, pady=10)
    quadro_banco.grid(row=1, column=0, sticky='we')

    table_validade = ttk.Treeview(quadro_validade)
    table_validade['columns'] = ('ID', 'Medicamento', 'Data de Validade', 'Vencido')
    table_validade.heading('#0', text='', anchor='w')
    table_validade.column('#0', width=0)
    table_validade.heading('ID', text='ID')
    table_validade.heading('Medicamento', text='Medicamento')
    table_validade.heading('Data de Validade', text='Data de Validade')
    table_validade.heading('Vencido', text='Vencido')

    table_banco = ttk.Treeview(quadro_banco)
    table_banco['columns'] = ('ID', 'Medicamento', 'Medida', 'Forma Farmacêutica', 'Quantidade')
    table_banco.heading('#0', text='', anchor='w')
    table_banco.column('#0', width=0)
    table_banco.heading('ID', text='ID')
    table_banco.heading('Medicamento', text='Medicamento')
    table_banco.heading('Medida', text='Medida')
    table_banco.heading('Forma Farmacêutica', text='Forma Farmacêutica')
    table_banco.heading('Quantidade', text='Quantidade')

    carregar2()

    table_validade.pack()

    carregar()

    table_banco.pack()

    quadro5 = LabelFrame(janela2, padx=10, pady=10, bg='pink', font='Verdana 18 italic', fg='purple')
    quadro5.grid(row=2, column=0, sticky='we')

    editar_quantidade_button = Button(quadro5, fg='purple', text="Editar Quantidade", command=editar_quantidade)
    editar_quantidade_button.grid(row=0, column=0, pady=10)

    voltar_menu_button = Button(quadro5, fg='purple', text="Voltar",anchor= 'e', command=lambda: [janela2.destroy(), voltar_menu()])
    voltar_menu_button.grid(row=0, column=1, pady=10,sticky='we')

    janela2.mainloop()

def voltar_menu():

    criar_janela_inicial()


def carregar2():
    conexao = sqlite3.connect('farmacia.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM data_farmacia")
    linhas = cursor.fetchall()
    table_validade.delete(*table_validade.get_children())

    hoje = datetime.date.today()  # Obter a data de hoje

    for linha in linhas:
        id, medicamento, data_validade = linha
        data_validade = datetime.datetime.strptime(data_validade, '%d/%m/%Y').date()  # Converter para objeto de data

        # Verificar se a data de validade expirou
        vencido = 'Sim' if data_validade < hoje else 'Não'

        table_validade.insert('', 'end', values=(id, medicamento, data_validade, vencido))

    conexao.close()


def carregar():
    conexao = sqlite3.connect('farmacia.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM banco_farmacia")
    linhas = cursor.fetchall()
    table_banco.delete(*table_banco.get_children())

    for linha in linhas:
        id, medicamento, medida, forma_farmaceutica, quantidade = linha
        table_banco.insert('', 'end', values=(id, medicamento, medida, forma_farmaceutica, quantidade))

    conexao.close()


def criar_janela_cadastro():

    global medicamento1, data_de_validade1, medida1, forma_farmaceutica1,quantidade1,quadrobotao,janela

    janela3.destroy()
    janela = Tk()
    janela.config(borderwidth=30)
    janela.title('Cadastro de produtos')
    janela.option_add('*Font', 'Arial 14')
    quadro = LabelFrame(janela,text=emoji.emojize(':ambulance: Cadastro de produtos'), padx=10, pady=10, font='Verdana 18 italic', fg='black', bg='pink')
    quadro.grid(row=0, column=0, sticky='we')
    quadrobotao = LabelFrame(janela,text='', padx=0, pady=0, bg='pink')
    quadrobotao.grid(row=1, column=0, sticky='NSWE')

    medicamento = Label(quadro, text='Medicamento:', font='Verdana 14 italic', anchor='e', bg='pink')
    medicamento.grid(row=0, column=0)
    medicamento1 = Entry(quadro)
    medicamento1.grid(row=0, column=1, columnspan=5, sticky='we')

    data_de_validade = Label(quadro, text='Data de validade:', font='Verdana 14 italic', anchor='e', bg='pink')
    data_de_validade.grid(row=1, column=4, sticky='we')
    data_de_validade1 = Entry(quadro)
    data_de_validade1.grid(row=1, column=5, sticky='e')

    medida = Label(quadro, text='Medida:', font='Verdana 14 italic', anchor='e', bg='pink')
    medida.grid(row=0, column=4, sticky='we')
    medida1 = Entry(quadro)
    medida1.grid(row=0, column=5, sticky='we')

    forma_farmaceutica = Label(quadro, text='Forma farmacêutica:', font='Verdana 14 italic', anchor='w', bg='pink')
    forma_farmaceutica.grid(row=1, column=0, sticky='e')
    forma_farmaceutica1 = Entry(quadro, width=15)
    forma_farmaceutica1.grid(row=1, column=1, sticky='e')

    quantidade = Label(quadro, text='Quantidade:', font='Verdana 14 italic', anchor='w', bg='pink')
    quantidade.grid(row=1, column=2, sticky='w')
    quantidade1 = Entry(quadro)
    quantidade1.grid(row=1, column=3, columnspan=1, sticky='e')

    botao = Button(quadrobotao, text='Salvar informações', font='Verdana 14 italic', anchor='e', command=salvar, fg='purple')
    botao.grid(row=6, column=0, sticky='e')

    botao1 = Button(quadrobotao, text=emoji.emojize('\u2190 Voltar'), font='Verdana 14 italic', anchor='e', width=7, fg='purple', command=lambda: [janela.destroy(), criar_janela_inicial()])
    botao1.grid(row=6, column=1, sticky='we')

    janela.mainloop()

def criar_janela_inicial():

    global janela3

    janela3 = Tk()
    janela3.title('CEFH (Controle de estoque Farmâcia Hospitalar) - Alpha 1.0')
    janela3.config(borderwidth=30)
    janela3.option_add('*Font', 'Arial 14')

    style = ThemedStyle(janela3)
    style.set_theme('arc')

    quadro = LabelFrame(janela3, text=emoji.emojize(':syringe: Menu Interativo'), padx=10, pady=10, bg='pink')
    quadro.grid(row=0, column=0, sticky='we')

    quadro_botoes = Frame(quadro, padx=10, pady=10)
    quadro_botoes.grid(row=1, column=0, sticky='e')

    lb_controle = Label(quadro, text='CONTROLE DE \n ESTOQUE FARMÂCIA HOSPITALAR', font='Verdana 20 italic',
                        anchor='e', background='pink')
    lb_controle.grid(row=0, column=0, columnspan=2, sticky='we')

    botao = Button(quadro_botoes, text=emoji.emojize(':package: Cadastrar Produtos'), anchor='w', fg='purple',
                   command=criar_janela_cadastro)
    botao.grid(row=2, column=0, sticky='we')

    botao2 = Button(quadro_botoes, text=emoji.emojize(':calendar: Validades e Estoque'), anchor='w', fg='purple',
                    command=lambda: [janela3.destroy(), avancar()])
    botao2.grid(row=2, column=1, sticky='we')

    janela3.mainloop()


criar_banco()
criar_janela_inicial()