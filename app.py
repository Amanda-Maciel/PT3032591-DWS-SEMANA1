from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Avaliação contínua: Aula 030</h1>
        <ul>
            <li><a href="{}">Home</a></li>
            <li><a href="{}">Identificação</a></li>
            <li><a href="{}">Contexto de Requisição</a></li>
        </ul>
    '''.format(
        url_for('home'),
        url_for('identificacao'),
        url_for('contexto')
    )

@app.route('/identificacao')
def identificacao():
    return '''
        <h1>Avaliação contínua: Aula 030</h1>
        <p><strong>Aluno:</strong> Amanda Maciel</p>
        <p><strong>Prontuário:</strong> PT3032591</p>
        <p><strong>Instituição:</strong> IFSP</p>
        <p><a href="{}">Voltar ao início</a></p>
    '''.format(url_for('home'))

@app.route('/contextorequisicao')
def contexto():
    navegador = request.headers.get('User-Agent')
    ip_remoto = request.remote_addr
    host = request.host  # ou request.host_url para incluir http(s)

    return '''
        <h1>Avaliação contínua: Aula 030</h1>
        <p><strong>Seu navegador é:</strong> {}</p>
        <p><strong>O IP do computador remoto é:</strong> {}</p>
        <p><strong>O host da aplicação é:</strong> {}</p>
        <p><a href="{}">Voltar ao início</a></p>
    '''.format(
        navegador,
        ip_remoto,
        host,
        url_for('home')
    )
