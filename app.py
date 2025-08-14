from flask import Flask, redirect, url_for, jsonify, abort

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World! Disciplina PTBDSWS'

@app.route('/user/Fabio Teixeira')
def user():
    return 'Hello, Fabio Teixeira!'

@app.route('/contextorequisicao')
def contexto():
    return 'Your browser is Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'

@app.route('/codigostatusdiferente')
def status_diferente():
    return 'Bad Request'

@app.route('/objetoresposta')
def objeto_resposta():
    return jsonify({'This document carries a cookie!'})

@app.route('/redirecionamento')
def redirecionamento():
    return redirect(url_for('https://ptb.ifsp.edu.br/'))

@app.route('/abortar')
def rota_abortada():
    abort(403)  

