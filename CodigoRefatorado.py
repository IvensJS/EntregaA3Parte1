import sqlite3
from tkinter import Tk, Label, Entry, Button, Frame, LabelFrame, END, messagebox
from ttkthemes import ThemedStyle

DB_NOME = 'plano_de_voo.db'
CAMPOS = [
    ('Aeronave', None),
    ('Prefixo', 'validar_prefixo'),
    ('Tipo de Voo (VFR/IFR)', 'validar_letras'),
    ('Regra de Voo', 'validar_letras'),
    ('Velocidade de Cruzeiro', None),
    ('Nível de Cruzeiro', None),
    ('Aeródromo de Partida', 'validar_letras'),
    ('Horário de Partida', 'validar_horario'),
    ('Rota', None),
    ('Aeródromo de Destino', None),
    ('Tempo Total de Voo', 'validar_horario'),
    ('Aeródromos Alternativos', 'validar_letras'),
    ('Autonomia', 'validar_horario'),
    ('Número de Pessoas a Bordo', 'validar_numeros'),
    ('Observações', None)
]

entradas = {}


# ========== BANCO DE DADOS ==========

def criar_banco():
    with sqlite3.connect(DB_NOME) as conexao:
        cursor = conexao.cursor()
        cursor.execute('DROP TABLE IF EXISTS plano_voo')
        cursor.execute('''
            CREATE TABLE plano_voo (
                id INTEGER PRIMARY KEY,
                Aeronave TEXT,
                Prefixo TEXT,
                Tipo_de_Voo TEXT,
                Regra_de_Voo TEXT,
                Velocidade_de_Cruzeiro TEXT,
                Nivel_de_Cruzeiro TEXT,
                Aerodromo_de_Partida TEXT,
                Horario_de_Partida TEXT,
                Rota TEXT,
                Aerodromo_de_Destino TEXT,
                Tempo_Total_de_Voo TEXT,
                Aerodromos_Alternativos TEXT,
                Autonomia TEXT,
                Numero_de_Pessoas_Bordo TEXT,
                Observacoes TEXT
            )
        ''')


# ========== VALIDAÇÕES ==========

def validar_letras(entry, valor):
    if not valor.isalpha():
        exibir_erro(entry, 'Este campo só aceita letras.')


def validar_numeros(entry, valor):
    if not valor.isdigit():
        exibir_erro(entry, 'Este campo só aceita números.')


def validar_horario(entry, valor):
    if not all(c.isdigit() or c == ':' for c in valor):
        exibir_erro(entry, 'Este campo só aceita números e ":" (dois pontos).')


def validar_prefixo(entry, valor):
    if any(c.isdigit() for c in valor):
        exibir_erro(entry, 'O prefixo não pode conter números.')


def exibir_erro(entry, mensagem):
    messagebox.showerror('Erro de Validação', mensagem)
    entry.delete(0, END)


# ========== ENVIO DO PLANO ==========

def enviar_plano():
    dados = [entrada.get() for entrada in entradas.values()]
    with sqlite3.connect(DB_NOME) as conexao:
        cursor = conexao.cursor()
        cursor.execute(f'''
            INSERT INTO plano_voo (
                Aeronave, Prefixo, Tipo_de_Voo, Regra_de_Voo, Velocidade_de_Cruzeiro, Nivel_de_Cruzeiro,
                Aerodromo_de_Partida, Horario_de_Partida, Rota, Aerodromo_de_Destino, Tempo_Total_de_Voo,
                Aerodromos_Alternativos, Autonomia, Numero_de_Pessoas_Bordo, Observacoes
            ) VALUES ({','.join(['?'] * 15)})
        ''', dados)

    messagebox.showinfo('Sucesso', 'Plano de voo enviado com sucesso!')
    limpar_campos()


def limpar_campos():
    for entry in entradas.values():
        entry.delete(0, END)


# ========== INTERFACE GRÁFICA ==========

def criar_rotulo_entrada(container, texto, linha, validacao_func):
    Label(container, text=texto, font='Verdana 14', anchor='e', bg='lightgrey').grid(
        row=linha, column=0, sticky='e', padx=5, pady=5
    )
    entry = Entry(container, font='Verdana 14')
    entry.grid(row=linha, column=1, columnspan=3, sticky='we', padx=5, pady=5)

    if validacao_func:
        entry.bind('<FocusOut>', lambda e: validacao_func(entry, entry.get()))

    return entry


def criar_janela_inicial():
    janela = Tk()
    janela.title('Envio de Plano de Voo')
    janela.config(borderwidth=30)

    style = ThemedStyle(janela)
    style.set_theme('breeze')

    quadro = LabelFrame(janela, text='Envio de Plano de Voo', padx=10, pady=10,
                        font='Verdana 18 bold', fg='darkblue', bg='lightgrey')
    quadro.grid(row=0, column=0, padx=10, pady=10, sticky='we')

    for i, (label, val_func) in enumerate(CAMPOS):
        func = globals().get(val_func) if val_func else None
        entradas[label] = criar_rotulo_entrada(quadro, label + ':', i, func)

    quadro_botoes = Frame(janela, padx=10, pady=10, bg='lightgrey')
    quadro_botoes.grid(row=1, column=0, sticky='we')

    Button(quadro_botoes, text='Enviar', font='Verdana 14', fg='white', bg='green',
           command=enviar_plano).grid(row=0, column=0, sticky='we', padx=5, pady=5)

    Button(quadro_botoes, text='Cancelar', font='Verdana 14', fg='white', bg='red',
           command=janela.destroy).grid(row=0, column=1, sticky='we', padx=5, pady=5)

    janela.mainloop()


# ========== EXECUÇÃO ==========

if __name__ == '__main__':
    criar_banco()
    criar_janela_inicial()
