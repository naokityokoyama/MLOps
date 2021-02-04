# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:10:30 2021

@author: Naoki
"""

from flask import Flask, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
colunas = ['tamanho', 'ano', 'garagem'] #colunas do predict usada dentro do list comprehetion
df = pd.read_csv('casas.csv')

X = df.drop('preco', axis=1)
y=df.preco

X_train, X_test , y_train, y_test = train_test_split(X,y ,test_size=0.3, random_state=42)
modelo = LinearRegression()

modelo.fit(X_train, y_train)

app = Flask(__name__)

@app.route('/cotacao/', methods=['POST']) # para passar json usamos o post

def cotacao():
    dados = request.get_json()
    dados_input = [dados[x] for x in colunas]
    preco = modelo.predict([dados_input])
    return jsonify(preco=preco[0])


app.run()