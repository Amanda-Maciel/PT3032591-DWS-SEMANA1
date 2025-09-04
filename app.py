from flask import Flask, url_for, request
from datetime import datetime

app = Flask(__name__)

base_html = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Avaliação contínua: Aula 040</title>
  <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a class="navbar-brand" href="#">Avaliação contínua: <strong>Aula 040</strong></a>
  <div class="collapse navbar-collapse">
    <ul class="navbar-nav ml-auto">
      <li class="nav-item"><a class="nav-link" href="{home}">Home</a></li>
      <li class="nav-item"><a class="nav-link" href="{ident}">Identificação</a></li>
      <li class="nav-item"><a class="nav-link" href="{contexto}">Contexto da requisição</a></li>
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

def tempo_relativo(segundos: int) -> str:
    """Transforma segundos em uma frase tipo 'a few seconds ago'."""
    if segundos < 5:
        return "That was a few seconds ago."
    elif segundos < 60:
        return f"That was {segundos} seconds ago."
    elif segundos < 120:
        return "That was 1 minute ago."
    else:
        minutos = segundos // 60
        return f"That was {minutos} minutes ago."

@app.route('/')
def home():
    agora = datetime.now()
    texto_data = agora.strftime("%B %d, %Y %I:%M %p")
    # calcula diferença em segundos entre agora e agora (vai ser zero ao carregar)
    segundos = (datetime.now() - agora).seconds
    conteudo = f'''
      <h1>Dados da última atualização:</h1>
      <hr>
      <p>The local date and time is {texto_data}.</p>
      <p>{tempo_relativo(segundos)}</p>
    '''
    return base_html.format(
        home=url_for('home'),
        ident=url_for('identificacao'),
        contexto=url_for('contexto'),
        conteudo=conteudo
    )

@app.route('/identificacao')
def identificacao():
    conteudo = '''
      <h1>Olá, Amanda Maciel!</h1>
      <hr>
      <p>Prontuário: PT3032591</p>
      <p>Instituição: IFSP</p>
    '''
    return base_html.format(
        home=url_for('home'),
        ident=url_for('identificacao'),
        contexto=url_for('contexto'),
        conteudo=conteudo
    )

@app.route('/contextorequisicao')
def contexto():
    navegador = request.headers.get('User-Agent')
    ip_remoto = request.remote_addr
    host = request.host
    conteudo = f'''
      <h1>Olá, Amanda Maciel!</h1>
      <hr>
      <p>Seu navegador é: {navegador}</p>
      <p>O IP do computador remoto é: {ip_remoto}</p>
      <p>O host da aplicação é: {host}</p>
    '''
    return base_html.format(
        home=url_for('home'),
        ident=url_for('identificacao'),
        contexto=url_for('contexto'),
        conteudo=conteudo
    )

@app.route('/user/<nome>/<prontuario>/IFSP')
def user_dinamico(nome, prontuario):
    conteudo = f'''
      <h1>Olá, {nome}!</h1>
      <hr>
      <p>Prontuário: {prontuario}</p>
      <p>Instituição: IFSP</p>
    '''
    return base_html.format(
        home=url_for('home'),
        ident=url_for('identificacao'),
        contexto=url_for('contexto'),
        conteudo=conteudo
    )

@app.route('/rotainexistente')
def rota_inexistente():
    conteudo = '<h1>Not Found</h1>'
    return base_html.format(
        home=url_for('home'),
        ident=url_for('identificacao'),
        contexto=url_for('contexto'),
        conteudo=conteudo
    )

if __name__ == '__main__':
    app.run(debug=True)
