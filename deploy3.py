# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:10:30 2021

@author: Naoki
"""

from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth #basica autenticação
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
colunas = ['tamanho', 'ano', 'garagem'] 
modelo = pickle.load(open('modelo.sav', 'rb'))

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'naoki'
app.config['BASIC_AUTH_PASSWORD'] = '1234'

basic_auth = BasicAuth(app)

@app.route('/cotacao/', methods=['POST']) # para passar json usamos o post
@basic_auth.required
def cotacao():
    dados = request.get_json()
    dados_input = [dados[x] for x in colunas]
    preco = modelo.predict([dados_input])
    return jsonify(preco=preco[0])


app.run()