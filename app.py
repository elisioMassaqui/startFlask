from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

#A primeira rota carrega nossa interface tipo um cardapio
#Onde os cliente vão poder escolher qual comida escolher
@app.route('/')
def index():
    return render_template('index.html')

#Os methods são todos resumidos com que o usuario vai fazer
#Se ele pedir uma comida é GET
#Se ele procurar pagar pela comida é POST
#Se ele aumentar o $ pra comer mais pratos é PUT
#Se ele deitar a comida pode ser Delete

#Comidas que estarão no cardapio

#Enviar comida pra o cliente comer
#Na hora de servidor enviar usa
# jsonify pra simplificar o processo
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "Hello from Flask"}
    return jsonify(data.get("message"))

#Pegar dinheiro pago pelo usuario
#Na hora de servidor receber usa
#uma função json raiz
@app.route('/api/data', methods=['POST'])
def post_data():
    #Com argumentos padrão e deve ser Aplication/json
    #Ou então 415 Unsupported Media Type error.
    data = request.json
    #E agora deve fazer o processamento dos dados
    return jsonify({"status": "sucess", "received": data})


if __name__ == "__main__":
    app.run(debug=True)