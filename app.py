from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import socket

app = Flask(__name__)


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

    return render_template("index.html", dados=dados_usuario)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        return redirect(url_for("acesso", usuario=usuario))

    now = datetime.now().strftime("%B %d, %Y %I:%M %p")
    return render_template("login.html", now=now)


@app.route("/acesso")
def acesso():
    usuario = request.args.get("usuario", "desconhecido")
    now = datetime.now().strftime("%B %d, %Y %I:%M %p")
    return render_template("acesso.html", usuario=usuario, now=now)


if __name__ == "__main__":
    app.run(debug=True)