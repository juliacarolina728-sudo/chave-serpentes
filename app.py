import os
from flask import Flask, render_template, request, redirect
import pg8000  

app = Flask(__name__)

DATABASE_URL = os.environ.get('DATABASE_PUBLIC_URL') or os.environ.get('DATABASE_URL')

def get_db_connection():
    return pg8000.connect(dsn=DATABASE_URL)

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
def sugestoes():  # <--- Corrigido aqui! Agora o url_for('sugestoes') vai funcionar perfeitamente
    return render_template('sugestoes.html')

@app.route('/enviar', methods=['POST'])
def enviar_sugestao():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        sugestao = request.form.get('sugestao')

        try:
            conn = get_db_connection()
            cur = conn.cursor()
            # Corrigido aqui: trocado %s por :1, :2, :3 para o pg8000 aceitar os dados
            cur.execute(
                "INSERT INTO sugestoes (nome, email, sugestao) VALUES (:1, :2, :3)",
                (nome, email, sugestao)
            )
            conn.commit()
            cur.close()
            conn.close()
            return "Sugestão enviada com sucesso!"
        except Exception as e:
            return f"Erro ao salvar no banco: {e}", 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))