from flask import Flask, request, url_for
from datetime import datetime
import socket

app = Flask(__name__)

# HTML base
base_html = '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Avaliação contínua: Aula 050.B</title>
  <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a class="navbar-brand" href="{home}"><strong>Avaliação contínua:</strong> Aula 050.B</a>
  <div class="collapse navbar-collapse">
    <ul class="navbar-nav ml-auto">
      <li class="nav-item"><a class="nav-link" href="{home}">Home</a></li>
      <li class="nav-item"><a class="nav-link" href="{login}">Login</a></li>
    </ul>
  </div>
</nav>
<div class="container mt-4">
  {conteudo}
</div>
</body>
</html>
'''

# Dados do usuário
dados_usuario = {
    "nome": "Estranho",
    "sobrenome": "",
    "instituicao": "None",
    "disciplina": "",
    "ip": "None",
    "host": "None"
}

@app.route("/", methods=["GET", "POST"])
def home():
    global dados_usuario

    if request.method == "POST":
        dados_usuario["nome"] = request.form.get("nome") or "Estranho"
        dados_usuario["sobrenome"] = request.form.get("sobrenome") or ""
        dados_usuario["instituicao"] = request.form.get("instituicao") or "None"
        dados_usuario["disciplina"] = request.form.get("disciplina") or ""
        dados_usuario["ip"] = request.remote_addr or "None"
        dados_usuario["host"] = socket.gethostname() or "None"

    now = datetime.now().strftime("%B %d, %Y %I:%M %p")

    conteudo = f"""
    <h2>Olá, {dados_usuario['nome']}!</h2>
    <p>A sua Instituição de ensino é {dados_usuario['instituicao']}</p>
    <p>Está cursando a disciplina de {dados_usuario['disciplina']}</p>
    <p>O IP do computador remoto é: {dados_usuario['ip']}</p>
    <p>O host da aplicação é: {dados_usuario['host']}</p>
    <hr>
    <form method="POST">
      <div class="form-group">
        <label>Informe o seu nome</label>
        <input type="text" class="form-control" name="nome">
      </div>
      <div class="form-group">
        <label>Informe o seu sobrenome:</label>
        <input type="text" class="form-control" name="sobrenome">
      </div>
      <div class="form-group">
        <label>Informe a sua Instituição de ensino:</label>
        <input type="text" class="form-control" name="instituicao">
      </div>
      <div class="form-group">
        <label>Informe a sua disciplina:</label>
        <select class="form-control" name="disciplina">
          <option value="DSWA5">DSWA5</option>
          <option value="DSWA4">DSWA4</option>
          <option value="Gestão De Projetos">Gestão de Projetos</option>
        </select>
      </div>
      <button type="submit" class="btn btn-light">Submit</button>
    </form>
    <p class="mt-3 text-muted">The local date and time is {now}.</p>
    <p class="text-muted">That was a few seconds ago.</p>
    """

    return base_html.format(
        home=url_for("home"),
        login=url_for("login"),
        conteudo=conteudo
    )

@app.route("/login", methods=["GET", "POST"])
def login():
    now = datetime.now().strftime("%B %d, %Y %I:%M %p")
    conteudo = f"""
    <h1>Login</h1>
    <form method="POST" class="form-inline mt-3">
        <input type="text" class="form-control mr-2" name="usuario" placeholder="Usuário">
        <button type="submit" class="btn btn-success">Entrar</button>
    </form>
    <p class="mt-3 text-muted">Data e hora atual: {now}</p>
    """
    return base_html.format(
        home=url_for("home"),
        login=url_for("login"),
        conteudo=conteudo
    )

if __name__ == "__main__":
    app.run(debug=True)
