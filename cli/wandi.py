from flask import Flask,jsonify
from chegamos import chegamos
from chegamos import chegamosJsonfy
from chegamos import criarPasta
from arduinoVersion import arduinoV

wandi = Flask(__name__)
print(wandi)

@wandi.route('/', methods=['GET'])
def Chegamos():
    chegamos(10, 30)
    return f'chegamos com lista e soma: {chegamos()}'

@wandi.route('/comJson', methods=['GET'])
def ChegamosJson():
    chegamosJsonfy(10, 30)
    return jsonify(chegamos())

@wandi.route('/criarP', methods=['GET'])
def CriarPasta():
    return jsonify(criarPasta())

@wandi.route('/arduinoVersion')
def arduinoVersion():
    return jsonify(arduinoV())
if __name__ == "__main__":
    wandi.run(debug=True, port=2002)