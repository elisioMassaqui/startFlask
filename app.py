from flask import Flask

web = Flask(__name__)

@web.route("/")
def HELLO():
    print('OI')
    TypeError = 5 #Erro de tipo recebido pelo navegador
    #A lista ele retornou pra navegador
    listaAceitavel = [1, 2, 3, 4, 5]
    #Mas o objecto não!
    x3 = {'nome': 'elisio', 'idade': 22}
    pegarTodasChaves = print(x3.keys())
    #AttributeError return  x3, listaAceitavel, pegarTodasChaves
    #talvez return f"""x3:{x3}, listaAceitavel:{listaAceitavel}, pegarTodasChaves{pegarTodasChaves}"""
    return  listaAceitavel, pegarTodasChaves, x3


if __name__ == "__main__":
    web.run(debug=True)