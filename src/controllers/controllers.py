from flask.views import MethodView
from flask import Flask, render_template, request, redirect, url_for
from src.db import sql_manager, Error


class Index(MethodView):
    def get(self):
        return render_template('index.html')

class Funcionario(MethodView):
    def get(self):
        return render_template('public/funcionario.html')


class Cargo(MethodView):
    def get(self):
        setor = sql_manager.execute_query("SELECT * FROM setor")
        return render_template('public/cargo.html', setor=setor)

    def post(self):
        nome = request.form['nome']
        setor_nome = request.form['setor']  
        data = (nome, setor_nome)
        query = "INSERT INTO cargo (nome, id_setor) VALUES (%s, %s)"

        try:
            sql_manager.execute_update(query, data)
            setor = sql_manager.execute_query("SELECT * FROM setor")
        except Error as e:
            error_message = "Ocorreu um erro durante a inserção: "
            setor = sql_manager.execute_query("SELECT * FROM setor")

        return render_template('public/cargo.html', setor=setor, error=error_message)
    
class Setor(MethodView):
    def get(self):
        return render_template('public/Setor.html')

    def post(self):
        nome = request.form['nome']
        data = (nome,)
        query = "INSERT INTO setor (nome) VALUES (%s)"
        success = sql_manager.execute_update(query, data)
        print(success)
        return render_template('public/Setor.html')
        

class Funcionario(MethodView):
    def get(self):
        cargos = sql_manager.execute_query("SELECT c.id AS id_cargo, c.nome AS nome_cargo, s.id AS id_setor, s.nome AS nome_setor FROM cargos AS c JOIN setor AS s ON c.id_setor = s.id")
        return render_template('public/funcionario.html', cargo=cargos)

    def post(self):
        primeiro_nome = request.form['primeiro_nome']
        sobrenome = request.form['sobrenome']  
        data_admissao = request.form['data_admissao']
        cargo_id, setor_id = request.form['cargo'].split('_')
        status_funcionario = request.form['status_funcionario']
        
        query = "INSERT INTO funcionarios (primeiro_nome, sobrenome, data_admissao, status_funcionario, id_setor, id_cargo) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (primeiro_nome, sobrenome, data_admissao, status_funcionario, setor_id, cargo_id,)
        error_message = None  # Inicialize a mensagem de erro como nula
        try:
            sql_manager.execute_update(query, data)
        except Error as e:
            error_message = "Ocorreu um erro durante a inserção: " + str(e)
        
        # Recupere os cargos, independentemente do sucesso ou falha
        cargos = sql_manager.execute_query("SELECT c.id AS id_cargo, c.nome AS nome_cargo, s.id AS id_setor, s.nome AS nome_setor FROM cargos AS c JOIN setor AS s ON c.id_setor = s.id")

        return render_template('public/funcionario.html', cargo=cargos, error=error_message)

