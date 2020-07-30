from flask import Flask, jsonify, request
from flask_cors import CORS
from controler import *
import json

from apiBelvo import *

api    = json.load( open('./belvo/config-api.json') )
client = Client( api['id'] , api['password'], api['endpoint'] )

app = Flask(__name__)

CORS(app)
cors = CORS(app, resources={
	r"/*": {
		"origins" : "*"
	}
})

@app.route( '/login', methods = ['POST'] )
def login():
	aux_login = 'admin'
	aux_senha = '12345'

	if request.is_json:
		data     = request.get_json()
		base     = ['login', 'senha']
		respKeys = list( data.keys() )
		if verificaChaves( base, respKeys ):
			if aux_login == data['login'] and aux_senha == data['senha']:
				return jsonify( rota_mensagem( "Acesso Liberado !" ) ), 200
			else:
				return jsonify( rota_mensagem( "Acesso Negado !" ) ), 403
		else:
			return jsonify( rota_mensagem("Parametros Invalidos !") ), 400
	else:
		return jsonify( rota_mensagem( "Aceita apenas POST em Json !" ) ), 400


@app.route( '/bancos', methods=['GET'] )
def empresas():
	return jsonify( getListEmpresas(client) )


@app.route( '/links', methods=['GET', 'POST'] )
def links():
	
	# Cria o Link
	if request.method == "POST":
		if request.is_json:
			data     = request.get_json()
			base     = ['banco', 'login', 'senha']
			respKeys = list( data.keys() )
			if verificaChaves( base, respKeys ):
				result = postNewLink( client, data['banco'], data['login'], data['senha'] )
				return jsonify( result ), 200
			else:
				return jsonify( rota_mensagem( "Paramentros Invalidos! Json necessario [ banco, login, senha ] !" ) ), 400
		else:
			return jsonify( rota_mensagem( "Precisa ser em Json, e prcisa dos parametros!" ) ), 400

	# Lista todos os Links
	if request.method == "GET":
		print( getAllLinks(client) )
		return jsonify( getAllLinks(client) ), 200


@app.route( '/contas', methods=['GET', 'POST'] )
def contas():

	# Lista todas as Contas
	if request.method == "GET":
		return jsonify( getAllContas( client ) )

		
if __name__ == '__main__':
    app.run(debug=True)