def rota_mensagem(mensagem):
	return {
		"mensagem" : f"{mensagem}"
	}

def verificaChaves(base, respose):
	if len( respose ) != len( base ):
		return False
	for i in base:
		if i not in respose:
			return False
	return True
