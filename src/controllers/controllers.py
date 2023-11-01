from flask.views import MethodView
from flask import Flask, render_template, request, redirect, url_for

class Index(MethodView):
    def get(self):
        return render_template('base.html')
    

class Funcionario(MethodView):
    def get(self):
        return render_template('funcionario.html')

class Cargo(MethodView):
    def get(self):
        return render_template('cargo.html')

class Setor(MethodView):
    def get(self):
        return render_template('Setor.html')

