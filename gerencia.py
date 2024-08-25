import tkinter as tk
from tkinter import messagebox, Toplevel, Text
from datetime import datetime
import sqlite3

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('financas.db')
cursor = conn.cursor()

# Criação da tabela de transações
cursor.execute('''
CREATE TABLE IF NOT EXISTS transacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT,
    categoria TEXT,
    valor REAL,
    data TEXT
)
''')
conn.commit()

# Função para adicionar transações ao banco de dados
def adicionar_transacao(tipo, categoria, valor, data):
    cursor.execute('''
    INSERT INTO transacoes (tipo, categoria, valor, data)
    VALUES (?, ?, ?, ?)
    ''', (tipo, categoria, valor, data))
    conn.commit()

# Função para obter o resumo das transações do banco de dados
def obter_resumo():
    cursor.execute('SELECT tipo, SUM(valor) FROM transacoes GROUP BY tipo')
    resumo = cursor.fetchall()
    return resumo

# Função para obter todas as despesas do banco de dados
def obter_despesas():
    cursor.execute('SELECT categoria, valor, data FROM transacoes WHERE tipo = "Despesa"')
    despesas = cursor.fetchall()
    return despesas

# Função para fechar a conexão com o banco de dados
def fechar_conexao():
    conn.close()

# Função para adicionar uma transação via interface
def adicionar_transacao_interface():
    tipo = var_tipo.get()
    categoria = entry_categoria.get()
    valor = entry_valor.get()
    data = datetime.now().strftime('%Y-%m-%d')
    
    if tipo and categoria and valor:
        adicionar_transacao(tipo, categoria, float(valor), data)
        messagebox.showinfo("Sucesso", "Transação adicionada com sucesso!")
        entry_categoria.delete(0, tk.END)
        entry_valor.delete(0, tk.END)
        atualizar_resumo()
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

# Função para atualizar o resumo das finanças
def atualizar_resumo():
    resumo = obter_resumo()
    texto_resumo = ""
    
    for tipo, valor in resumo:
        texto_resumo += f"{tipo.capitalize()}: R$ {valor:.2f}\n"
    
    label_resumo.config(text=texto_resumo)

# Função para gerar relatório de despesas
def gerar_relatorio_despesas():
    despesas = obter_despesas()
    if not despesas:
        messagebox.showinfo("Relatório", "Não há despesas registradas.")
        return
    
    # Criar uma nova janela para exibir o relatório
    janela_relatorio = Toplevel(janela)
    janela_relatorio.title("Relatório de Despesas")

    # Caixa de texto para mostrar as despesas
    text_relatorio = Text(janela_relatorio, wrap=tk.WORD, width=50, height=20)
    text_relatorio.pack()

    # Preencher a caixa de texto com as despesas
    for categoria, valor, data in despesas:
        text_relatorio.insert(tk.END, f"Categoria: {categoria}\nValor: R$ {valor:.2f}\nData: {data}\n\n")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Gerenciador de Finanças Pessoais")

# Widgets para adicionar transações
label_tipo = tk.Label(janela, text="Tipo")
label_tipo.pack()

var_tipo = tk.StringVar(value="Receita")
radio_receita = tk.Radiobutton(janela, text="Receita", variable=var_tipo, value="Receita")
radio_receita.pack()
radio_despesa = tk.Radiobutton(janela, text="Despesa", variable=var_tipo, value="Despesa")
radio_despesa.pack()

label_categoria = tk.Label(janela, text="Categoria")
label_categoria.pack()
entry_categoria = tk.Entry(janela)
entry_categoria.pack()

label_valor = tk.Label(janela, text="Valor")
label_valor.pack()
entry_valor = tk.Entry(janela)
entry_valor.pack()

botao_adicionar = tk.Button(janela, text="Adicionar Transação", command=adicionar_transacao_interface)
botao_adicionar.pack()

# Botão para gerar o relatório de despesas
botao_relatorio = tk.Button(janela, text="Gerar Relatório de Despesas", command=gerar_relatorio_despesas)
botao_relatorio.pack()

# Widget para exibir o resumo financeiro
label_resumo = tk.Label(janela, text="Resumo Financeiro", font=("Arial", 14))
label_resumo.pack()

# Atualizar o resumo das finanças ao iniciar a aplicação
atualizar_resumo()

# Iniciar a aplicação
janela.mainloop()

# Fechar a conexão com o banco de dados ao encerrar o programa
fechar_conexao()
