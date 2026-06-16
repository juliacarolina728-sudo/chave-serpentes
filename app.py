import os
from flask import Flask, render_template, request, redirect
import pg8000 
from urllib.parse import urlparse  # Biblioteca nativa do Python para desmembrar URLs

app = Flask(__name__)

# Pega o link do banco fornecido pelo Railway
DATABASE_URL = os.environ.get('DATABASE_PUBLIC_URL') or os.environ.get('DATABASE_URL')

def get_db_connection():
    # Quebra a URL do banco em partes (usuario, senha, host, porta, banco)
    url = urlparse(DATABASE_URL)
    
    # Conecta passando cada parâmetro no seu devido lugar de forma infalível
    return pg8000.connect(
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port,
        database=url.path[1:]  # O path vem como '/nome_do_banco', o [1:] remove a barra
    )

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

        conn = get_db_connection()
        cur = conn.cursor()
        
        # CORREÇÃO AQUI: Mudado de :nome para %s, e os dados passados em uma tupla ( )
        cur.execute(
            "INSERT INTO sugestoes (nome, email, sugestao) VALUES (%s, %s, %s)",
            (nome, email, sugestao)
        )
        
        conn.commit()
        cur.close()
        conn.close()
        
        return "Sugestão enviada com sucesso! Verifique seu banco de dados."
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))