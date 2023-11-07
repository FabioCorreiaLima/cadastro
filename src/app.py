from flask import Flask, render_template, request, redirect, url_for
from src.routes.routes import *

app = Flask(__name__)
app.config['STATIC_FOLDER'] = 'static'

app.add_url_rule(routes["index"], view_func=Index.as_view("index"))
app.add_url_rule(routes["funcionario"], view_func=Funcionario.as_view('funcionario'))
app.add_url_rule(routes["cargo"], view_func=Cargo.as_view('cargo'))
app.add_url_rule(routes["setor"], view_func=Setor.as_view('setor'))





# @app.route('/')
# def index():
    
#     return render_template('base.html')

# @app.route('/setor', methods=['GET', 'POST'])
# def setor():
#     if request.method == 'POST':
#         nome = request.form['nome']

#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO setor (nome) VALUES (%s)", (nome,))
#         mysql.connection.commit()
#         cur.close()

#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM setor")
#     setores = cur.fetchall()
#     cur.close()

#     return render_template('setor.html', setores=setores)

# @app.route('/funcionarios', methods=['GET', 'POST'])
# def funcionarios():
#     if request.method == 'POST':
#         primeiro_nome = request.form['primeiro_nome']
#         sobrenome = request.form['sobrenome']
#         data_admissao = request.form['data_admissao']
#         status_funcionario = request.form['status_funcionario']  # Obtemos o valor dos botões de opção

#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO funcionarios (primeiro_nome, sobrenome, data_admissao, status_funcionario) VALUES (%s, %s, %s, %s, %s, %s)", (primeiro_nome, sobrenome, data_admissao, status_funcionario))
#         mysql.connection.commit()
#         cur.close()

#     return render_template('funcionarios.html')

# @app.route('/cargos', methods=['GET', 'POST'])
# def cargos():
#     if request.method == 'POST':
#         nome = request.form['nome']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO cargos (nome) VALUES (%s)", (nome,))
#         mysql.connection.commit()
#         cur.close()

#     return render_template('cargos.html')

