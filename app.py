from flask import Flask

web = Flask(__name__)

@web.route("/")
def HELLO():
    print('OI')
    y = 'variavel y'
    z = 4505
    TypeError = 5 #Erro de tipo recebido pelo navegador
    #A lista ele retornou pra navegador
    listaAceitavel = [1, 2, 3, 4, 5, 'eliso', True, False, not True, 3.78, y, z]
    #Mas o objecto não!
    x3 = {'nome': 'elisio', 'idade': 22}
    printTodasChaves = print(x3.keys())
    pegarTodasChaves = x3.keys()
    #AttributeError return  x3, listaAceitavel, pegarTodasChaves
    #talvez return f"""x3:{x3}, listaAceitavel:{listaAceitavel}, pegarTodasChaves{pegarTodasChaves}"""
    return  listaAceitavel, x3


if __name__ == "__main__":
    web.run(debug=True)