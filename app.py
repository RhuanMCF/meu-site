# app.py
from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

# Caminho da pasta atual (onde está o app.py)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Função para ler o HTML direto do arquivo
def ler_html(nome_arquivo):
    caminho = os.path.join(BASE_DIR, nome_arquivo)
    with open(caminho, 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/')
def index():
    html = ler_html('index.html')
    return render_template_string(html)

@app.route('/bruno')
def bruno():
    html = ler_html('bruno.html')
    return render_template_string(html)

@app.route('/ícaro')
def cicero():
    html = ler_html('ícaro.html')
    return render_template_string(html)

@app.route('/admin')
def admin():
    html = ler_html('admin.html')
    return render_template_string(html)

# Servir as imagens direto da pasta
@app.route('/<path:caminho>')
def servir_arquivos(caminho):
    # Serve imagens, css, js etc que estiverem em subpastas ou na raiz
    if caminho.endswith(('.png', '.jpg', '.jpeg', '.gif', '.css', '.js')):
        return send_from_directory(BASE_DIR, caminho)
    return "Arquivo não encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)