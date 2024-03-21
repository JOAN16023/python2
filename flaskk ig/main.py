from flask import Flask

app = Flask(__name__)

@app.route('/')

def hola_mundo():
    return 'Hola Mundo!'
    
    
@app.route('/dojo')
def show_dojo():
    return 'Dojo!'

@app.route('/say/flaskk')
def show_():
    return 'Hola flask!'


if __name__=="__main__":
    app.run()