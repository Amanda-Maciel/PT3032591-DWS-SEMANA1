from flask import Flask, request, url_for

app = Flask(__name__)

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
  <a class="navbar-brand" href="{flasky}">Flasky</a>
  <div class="collapse navbar-collapse">
    <ul class="navbar-nav ml-auto">
      <li class="nav-item"><a class="nav-link" href="{home}">Home</a></li>
    </ul>
  </div>
</nav>
<div class="container mt-4">
  {conteudo}
</div>
</body>
</html>
'''

def render_form(nome=None):
    """Função para reaproveitar o mesmo formulário em Home e Flasky"""
    if nome:
        return f"<h1>Hello, {nome}!</h1>"
    return '''
      <h1>Hello, what is your name?</h1>
      <form method="POST" class="form-inline mt-3">
        <input type="text" class="form-control mr-2" name="nome" placeholder="Enter your name">
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    '''

@app.route('/', methods=["GET", "POST"])
def home():
    nome = request.form.get("nome")
    conteudo = render_form(nome)
    return base_html.format(
        home=url_for('home'),
        flasky=url_for('flasky'),
        conteudo=conteudo
    )

@app.route('/flasky', methods=["GET", "POST"])
def flasky():
    nome = request.form.get("nome")
    conteudo = render_form(nome)
    return base_html.format(
        home=url_for('home'),
        flasky=url_for('flasky'),
        conteudo=conteudo
    )

if __name__ == '__main__':
    app.run(debug=True)
