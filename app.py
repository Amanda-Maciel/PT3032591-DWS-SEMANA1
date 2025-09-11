from flask import Flask, request, url_for

app = Flask(__name__)

base_html = '''
<!DOCTYPE html>
<html lang="en">
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
</body>
</html>
'''

@app.route('/')
def home():
    conteudo = "<h1>Home</h1>"
    return base_html.format(
        home=url_for('home'),
        ident=url_for('identificacao'),
        contexto=url_for('contexto'),
        conteudo=conteudo
    )

@app.route('/identificacao', methods=["GET", "POST"])
def identificacao():
    nome = request.form.get("nome")
    if nome:
        conteudo = f"<h1>Hello, {nome}!</h1>"
    else:
        conteudo = '''
          <h1>Hello, what is your name?</h1>
          <form method="POST" class="form-inline mt-3">
            <input type="text" class="form-control mr-2" name="nome" placeholder="Enter your name">
            <button type="submit" class="btn btn-primary">Submit</button>
          </form>
        '''
    return base_html.format(
        home=url_for('home'),
        ident=url_for('identificacao'),
        contexto=url_for('contexto'),
        conteudo=conteudo
    )

@app.route('/contextorequisicao')
def contexto():
    conteudo = "<h1>Contexto da requisição</h1>"
    return base_html.format(
        home=url_for('home'),
        ident=url_for('identificacao'),
        contexto=url_for('contexto'),
        conteudo=conteudo
    )

if __name__ == '__main__':
    app.run(debug=True)
