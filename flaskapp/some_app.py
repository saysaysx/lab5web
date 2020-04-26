from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def hello():
    return " <html><head></head> <body> Hello World! </body></html>"
import threading
if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000)

from flask import render_template

@app.route("/data_to")
def data_to():
    some_pars = {'user':'Ivan','color':'red'}
    some_str = 'Hello my dear friends!'
    some_value = 10
    #передаем данные в шаблон
    return render_template('simple.html',some_str = some_str,some_value = some_value,some_pars=some_pars)


@app.route("/net")
def net():
    return render_template('net.html')

