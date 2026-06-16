import os
from flask import Flask, render_template, request, redirect
import pg8000  
from pg8000.dbapi import from_url
app = Flask(__name__)

# Pega o link do banco fornecido pelo Railway
DATABASE_URL = os.environ.get('DATABASE_PUBLIC_URL') or os.environ.get('DATABASE_URL')

def get_db_connection():
    # CORREÇÃO CRUCIAL: Trocado de .connect(dsn=...) para .from_url(...)
    # Isso faz o pg8000 quebrar a URL do Railway em partes automaticamente
    return pg8000.from_url(DATABASE_URL)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/identificacao')
def identificacao():
    return render_template('identificacao.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/sugestoes')
def sugestoes():  
    return render_template('sugestoes.html')

@app.route('/enviar', methods=['POST'])
def enviar_sugestao():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        sugestao = request.form.get('sugestao')

        # Mantendo sem o try/except para monitorarmos qualquer outro detalhe direto na tela
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Inserção correta usando named parameters (formato dicionário)
        cur.execute(
            "INSERT INTO sugestoes (nome, email, sugestao) VALUES (:nome, :email, :sugestao)",
            {"nome": nome, "email": email, "sugestao": sugestao}
        )
        
        conn.commit()
        cur.close()
        conn.close()
        
        return "Sugestão enviada com sucesso! Verifique seu banco de dados."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))