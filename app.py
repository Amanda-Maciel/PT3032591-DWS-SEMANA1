from flask import Flask, url_for, request
from datetime import datetime

app = Flask(__name__)

base_html = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Avaliação Contínua</title>
    <link rel="stylesheet" 
          href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="#">Flasky</a>
        <div class="collapse navbar-collapse">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item"><a class="nav-link" href="{home}">Home</a></li>
            </ul>
        </div>
    </nav>
    <div class="container mt-4">
        {conteudo}
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''

@app.route('/')
def home():
    agora = datetime.now().strftime("%B %d, %Y %I:%M %p")
    conteudo = f'''
        <h1>Hello World!</h1>
        <p>The local date and time is {agora}.</p>
    '''
    return base_html.format(
        home=url_for('home'),
        conteudo=conteudo
    )

@app.route('/identificacao')
def identificacao():
    conteudo = '''
        <h1>Identificação</h1>
        <p><strong>Aluno:</strong> Amanda Maciel</p>
        <p><strong>Prontuário:</strong> PT3032591</p>
        <p><strong>Instituição:</strong> IFSP</p>
    '''
    return base_html.format(
        home=url_for('home'),
        conteudo=conteudo
    )

@app.route('/contextorequisicao')
def contexto():
    navegador = request.headers.get('User-Agent')
    ip_remoto = request.remote_addr
    host = request.host  
    conteudo = f'''
        <h1>Contexto da Requisição</h1>
        <p><strong>Seu navegador é:</strong> {navegador}</p>
        <p><strong>O IP do computador remoto é:</strong> {ip_remoto}</p>
        <p><strong>O host da aplicação é:</strong> {host}</p>
    '''
    return base_html.format(
        home=url_for('home'),
        conteudo=conteudo
    )

# Rota /user/amandamaciel
@app.route('/user/amandamaciel')
def user_amanda():
    agora = datetime.now().strftime("%B %d, %Y %I:%M %p")
    conteudo = f'''
        <h1>Hello Amanda Maciel!</h1>
        <p>The local date and time is {agora}.</p>
    '''
    return base_html.format(
        home=url_for('home'),
        conteudo=conteudo
    )

@app.route('/rotainexistente')
def rota_inexistente():
    conteudo = '<h1>Not Found</h1>'
    return base_html.format(
        home=url_for('home'),
        conteudo=conteudo
    )

