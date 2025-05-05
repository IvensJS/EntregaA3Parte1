from tkinter import *
import sqlite3

def criar_banco():
    conexao = sqlite3.connect('planos_voo.db')
    cursor = conexao.cursor()

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS planos_voo
                    (
                    aeronave TEXT,
                    prefixo TEXT,
                    tipo_voo TEXT,
                    rota TEXT,
                    horario_previsto TEXT,
                    nivel_voo TEXT,
                    velocidade_voo TEXT,
                    piloto_comandante TEXT,
                    copiloto TEXT,
                    observacoes TEXT
                    )
                   ''')

    conexao.commit()
    conexao.close()

def enviar_plano_voo():
    conexao = sqlite3.connect('planos_voo.db')
    cursor = conexao.cursor()

    cursor.execute('''
    INSERT INTO planos_voo
    (aeronave, prefixo, tipo_voo, rota, horario_previsto, nivel_voo, velocidade_voo, piloto_comandante, copiloto, observacoes)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (en_aeronave.get(),
                    en_prefixo.get(),
                    en_tipo_voo.get(),
                    en_rota.get(),
                    en_horario_previsto.get(),
                    en_nivel_voo.get(),
                    en_velocidade_voo.get(),
                    en_piloto_comandante.get(),
                    en_copiloto.get(),
                    en_observacoes.get("1.0", END))
                   )

    conexao.commit()
    conexao.close()

# chamada da função criar_banco
criar_banco()

# inicio interface gráfica
janela = Tk()
janela.title('Envio de Plano de Voo')
janela.config(padx=10, pady=10)
janela.option_add('*Font', 'Verdana 12')

# Labels Frame
dados_plano_voo = LabelFrame(janela, text='Dados do Plano de Voo', padx=10, pady=10)
dados_plano_voo.grid(row=0, column=0, sticky='we')

# Widgets LabelFrame 'dados_plano_voo'
lb_aeronave = Label(dados_plano_voo, text='Aeronave:', anchor='e')
lb_aeronave.grid(row=0, column=0, sticky='we')

en_aeronave = Entry(dados_plano_voo)
en_aeronave.grid(row=0, column=1, columnspan=3, sticky='we')

lb_prefixo = Label(dados_plano_voo, text='Prefixo:', anchor='e')
lb_prefixo.grid(row=1, column=0, sticky='we')

en_prefixo = Entry(dados_plano_voo)
en_prefixo.grid(row=1, column=1)

lb_tipo_voo = Label(dados_plano_voo, text='Tipo de Voo (VFR/IFR):', anchor='e')
lb_tipo_voo.grid(row=1, column=2, sticky='we')

en_tipo_voo = Entry(dados_plano_voo)
en_tipo_voo.grid(row=1, column=3)

lb_rota = Label(dados_plano_voo, text='Rota:', anchor='e')
lb_rota.grid(row=2, column=0, sticky='we')

en_rota = Entry(dados_plano_voo)
en_rota.grid(row=2, column=1, columnspan=3, sticky='we')

lb_horario_previsto = Label(dados_plano_voo, text='Horário Previsto:', anchor='e')
lb_horario_previsto.grid(row=3, column=0, sticky='we')

en_horario_previsto = Entry(dados_plano_voo)
en_horario_previsto.grid(row=3, column=1)

lb_nivel_voo = Label(dados_plano_voo, text='Nível de Voo:', anchor='e')
lb_nivel_voo.grid(row=3, column=2, sticky='we')

en_nivel_voo = Entry(dados_plano_voo)
en_nivel_voo.grid(row=3, column=3)

lb_velocidade_voo = Label(dados_plano_voo, text='Velocidade de Voo:', anchor='e')
lb_velocidade_voo.grid(row=4, column=0, sticky='we')

en_velocidade_voo = Entry(dados_plano_voo)
en_velocidade_voo.grid(row=4, column=1)

lb_piloto_comandante = Label(dados_plano_voo, text='Piloto Comandante:', anchor='e')
lb_piloto_comandante.grid(row=4, column=2, sticky='we')

en_piloto_comandante = Entry(dados_plano_voo)
en_piloto_comandante.grid(row=4, column=3)

lb_copiloto = Label(dados_plano_voo, text='Copiloto:', anchor='e')
lb_copiloto.grid(row=4, column=0, sticky='we')

en_copiloto = Entry(dados_plano_voo)
en_copiloto.grid(row=5, column=1, columnspan=3, sticky='we')

lb_observacoes = Label(dados_plano_voo, text='Observações:', anchor='e')
lb_observacoes.grid(row=6, column=0, sticky='we')

en_observacoes = Text(dados_plano_voo, height=5)
en_observacoes.grid(row=6, column=1, columnspan=3, sticky='we')

# widgets Frame 'quadro_botoes'
quadro_botoes = Frame(janela, padx=10, pady=10)
quadro_botoes.grid(row=1, column=0, sticky='e')

bt_enviar = Button(quadro_botoes, text='Enviar', command=enviar_plano_voo)
bt_enviar.grid(row=0, column=0)

bt_cancelar = Button(quadro_botoes, text='Cancelar', command=janela.quit)
bt_cancelar.grid(row=0, column=1)

janela.mainloop()
