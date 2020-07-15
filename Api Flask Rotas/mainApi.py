from flask import Flask, jsonify, request
from flask_cors import CORS
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

@app.route('/bancos', methods=['GET'] )
def empresas():
	return jsonify( getListEmpresas(client) )


@app.route('/links', methods=['GET'] )
def links():

	if request.is_json :
		return request.get_json()
	else:
		return jsonify( getAllLinks(client) )



if __name__ == '__main__':
    app.run(debug=True)