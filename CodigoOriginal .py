from tkinter import ttk
from tkinter import *
import sqlite3
from tkinter import messagebox
from ttkthemes import ThemedStyle

def criar_banco():
    conexao = sqlite3.connect('plano_de_voo.db')
    cursor = conexao.cursor()
    # Primeiro, excluir a tabela existente, se houver
    cursor.execute('DROP TABLE IF EXISTS plano_voo')
    # Criar a tabela com a estrutura correta
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
    conexao.commit()
    conexao.close()

def enviar_plano():
    conexao = sqlite3.connect('plano_de_voo.db')
    cursor = conexao.cursor()
    cursor.execute(
        '''INSERT INTO plano_voo (Aeronave, Prefixo, Tipo_de_Voo, Regra_de_Voo, Velocidade_de_Cruzeiro, Nivel_de_Cruzeiro, Aerodromo_de_Partida, Horario_de_Partida, Rota, Aerodromo_de_Destino, Tempo_Total_de_Voo, Aerodromos_Alternativos, Autonomia, Numero_de_Pessoas_Bordo, Observacoes)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
        (aeronave_entry.get(), prefixo_entry.get(), tipo_de_voo_entry.get(), regra_de_voo_entry.get(), velocidade_de_cruzeiro_entry.get(), nivel_de_cruzeiro_entry.get(), aerodromo_de_partida_entry.get(), horario_de_partida_entry.get(), rota_entry.get(), aerodromo_de_destino_entry.get(), tempo_total_de_voo_entry.get(), aerodromos_alternativos_entry.get(), autonomia_entry.get(), numero_de_pessoas_bordo_entry.get(), observacoes_entry.get())
    )
    conexao.commit()
    conexao.close()

    messagebox.showinfo('Sucesso', 'Plano de voo enviado com sucesso!')

    # Limpar campos
    aeronave_entry.delete(0, END)
    prefixo_entry.delete(0, END)
    tipo_de_voo_entry.delete(0, END)
    regra_de_voo_entry.delete(0, END)
    velocidade_de_cruzeiro_entry.delete(0, END)
    nivel_de_cruzeiro_entry.delete(0, END)
    aerodromo_de_partida_entry.delete(0, END)
    horario_de_partida_entry.delete(0, END)
    rota_entry.delete(0, END)
    aerodromo_de_destino_entry.delete(0, END)
    tempo_total_de_voo_entry.delete(0, END)
    aerodromos_alternativos_entry.delete(0, END)
    autonomia_entry.delete(0, END)
    numero_de_pessoas_bordo_entry.delete(0, END)
    observacoes_entry.delete(0, END)

def criar_janela_inicial():
    global aeronave_entry, prefixo_entry, tipo_de_voo_entry, regra_de_voo_entry, velocidade_de_cruzeiro_entry, nivel_de_cruzeiro_entry, aerodromo_de_partida_entry, horario_de_partida_entry, rota_entry, aerodromo_de_destino_entry, tempo_total_de_voo_entry, aerodromos_alternativos_entry, autonomia_entry, numero_de_pessoas_bordo_entry, observacoes_entry

    janela = Tk()
    janela.title('Envio de Plano de Voo')
    janela.config(borderwidth=30)

    style = ThemedStyle(janela)
    style.set_theme('breeze')

    quadro = LabelFrame(janela, text='Envio de Plano de Voo', padx=10, pady=10, font='Verdana 18 bold', fg='darkblue', bg='lightgrey')
    quadro.grid(row=0, column=0, padx=10, pady=10, sticky='we')

    # Funções de validação
    def validar_letras(entry, texto):
        if not texto.isalpha():
            messagebox.showerror('Erro de Validação', 'Este campo só aceita letras.')
            entry.delete(0, END)

    def validar_numeros(entry, texto):
        if not texto.isdigit():
            messagebox.showerror('Erro de Validação', 'Este campo só aceita números.')
            entry.delete(0, END)

    def validar_horario(entry, texto):
        if not all(c.isdigit() or c == ':' for c in texto):
            messagebox.showerror('Erro de Validação', 'Este campo só aceita números e ":" (dois pontos).')
            entry.delete(0, END)

    def validar_prefixo(entry, texto):
        if any(c.isdigit() for c in texto):
            messagebox.showerror('Erro de Validação', 'O prefixo não pode conter números.')
            entry.delete(0, END)

    # Campo de entrada
    def criar_rotulo_entrada(quadro, texto, linha, validacao=None):
        Label(quadro, text=texto, font='Verdana 14', anchor='e', bg='lightgrey').grid(row=linha, column=0, sticky='e', padx=5, pady=5)
        entrada = Entry(quadro, font='Verdana 14')
        entrada.grid(row=linha, column=1, columnspan=3, sticky='we', padx=5, pady=5)
        if validacao:
            entrada.bind('<FocusOut>', lambda e: validacao(entrada, entrada.get()))
        return entrada

    aeronave_entry = criar_rotulo_entrada(quadro, 'Aeronave:', 0)
    prefixo_entry = criar_rotulo_entrada(quadro, 'Prefixo:', 1, validar_prefixo)
    tipo_de_voo_entry = criar_rotulo_entrada(quadro, 'Tipo de Voo (VFR/IFR):', 2, validar_letras)
    regra_de_voo_entry = criar_rotulo_entrada(quadro, 'Regra de Voo:', 3, validar_letras)
    velocidade_de_cruzeiro_entry = criar_rotulo_entrada(quadro, 'Velocidade de Cruzeiro:', 4)
    nivel_de_cruzeiro_entry = criar_rotulo_entrada(quadro, 'Nível de Cruzeiro:', 5)
    aerodromo_de_partida_entry = criar_rotulo_entrada(quadro, 'Aeródromo de Partida:', 6, validar_letras)
    horario_de_partida_entry = criar_rotulo_entrada(quadro, 'Horário de Partida:', 7, validar_horario)
    rota_entry = criar_rotulo_entrada(quadro, 'Rota:', 8)
    aerodromo_de_destino_entry = criar_rotulo_entrada(quadro, 'Aeródromo de Destino:', 9)
    tempo_total_de_voo_entry = criar_rotulo_entrada(quadro, 'Tempo Total de Voo:', 10, validar_horario)
    aerodromos_alternativos_entry = criar_rotulo_entrada(quadro, 'Aeródromos Alternativos:', 11, validar_letras)
    autonomia_entry = criar_rotulo_entrada(quadro, 'Autonomia:', 12, validar_horario)
    numero_de_pessoas_bordo_entry = criar_rotulo_entrada(quadro, 'Número de Pessoas a Bordo:', 13, validar_numeros)
    observacoes_entry = criar_rotulo_entrada(quadro, 'Observações:', 14)

    # Botões
    quadro_botoes = Frame(janela, padx=10, pady=10, bg='lightgrey')
    quadro_botoes.grid(row=1, column=0, sticky='we')

    enviar_button = Button(quadro_botoes, text='Enviar', font='Verdana 14', fg='white', bg='green', command=enviar_plano)
    enviar_button.grid(row=0, column=0, sticky='we', padx=5, pady=5)

    cancelar_button = Button(quadro_botoes, text='Cancelar', font='Verdana 14', fg='white', bg='red', command=janela.destroy)
    cancelar_button.grid(row=0, column=1, sticky='we', padx=5, pady=5)

    janela.mainloop()

criar_banco()
criar_janela_inicial()

