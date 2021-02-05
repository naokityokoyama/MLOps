from flask import Flask
from textblob import TextBlob
from flask_basicauth import BasicAuth 

app = Flask(__name__)  #Instânciando o Flask por convensão se usa o nome (__name__)

app.config['BASIC_AUTH_USERNAME'] = 'naoki'
app.config['BASIC_AUTH_PASSWORD'] = '1234'


@app.route('/')  #rota na barra de endereço


def ola(): #Pode se usar qualquer nome na função
    return ('minha primeira api')

basic_auth = BasicAuth(app)

@app.route('/sentimento/<frase>')
@basic_auth.required
def sentimento(frase):   #criando uma função simples de analise de sentimento
    tb = TextBlob(frase)
    tb_eng = tb.translate(to='en')
    polaridade = tb_eng.sentiment.polarity
    return "polaridade: {}".format(polaridade)

app.run(host='0.0.0.0') 