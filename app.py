from flask import Flask, request, redirect, url_for
from datetime import datetime
import socket

app = Flask(__name__)

# Modelo de base HTML
base_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Flasky</title>
  <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css">
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a class="navbar-brand" href="{home}">Flasky</a>
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

# Dicionário de dados do usuário
dados_usuario = {
    "nome": "Estranho",
    "sobrenome": "",
    "instituicao": "None",
    "disciplina": "",
    "ip": "None",
    "host": "None"
}

# ---------- ROTAS ----------
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

    conteudo = f"""
    <h1>Cadastro de Usuário</h1>
    <form method="POST" class="mt-3">
        <input type="text" name="nome" class="form-control mb-2" placeholder="Nome">
        <input type="text" name="sobrenome" class="form-control mb-2" placeholder="Sobrenome">
        <input type="text" name="instituicao" class="form-control mb-2" placeholder="Instituição">
        <input type="text" name="disciplina" class="form-control mb-2" placeholder="Disciplina">
        <button type="submit" class="btn btn-primary">Salvar</button>
    </form>
    <hr>
    <h4>Dados salvos:</h4>
    <pre>{dados_usuario}</pre>
    """

    return base_html.format(
        home=url_for("home"),
        login=url_for("login"),
        conteudo=conteudo
    )

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario") or "desconhecido"
        return redirect(url_for("acesso", usuario=usuario))

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

@app.route("/acesso")
def acesso():
    usuario = request.args.get("usuario", "desconhecido")
    now = datetime.now().strftime("%B %d, %Y %I:%M %p")
    conteudo = f"""
    <h1>Acesso liberado</h1>
    <p>Bem-vindo, <strong>{usuario}</strong>!</p>
    <p>Data e hora: {now}</p>
    """
    return base_html.format(
        home=url_for("home"),
        login=url_for("login"),
        conteudo=conteudo
    )

if __name__ == "__main__":
    app.run(debug=True)
