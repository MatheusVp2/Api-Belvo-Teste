from pprint import pprint
from belvo.client import Client


def getListEmpresas(client):
	"""
	Retorna todas a empresas cadastradas na API
	"""
	return list( client.Institutions.list() )


def getAllLinks(client):
	"""
	Retorna todos os Links
	"""
	return list( client.Links.list() )

def getEmpresaLinks(client, empresa):
	"""
	Retorna somente o Link Escolhido
	"""
	return list(client.Links.list( institution = empresa ))

def getEmpresasLinks(client, empresas):
	"""
	Retorna Lista de Links escolhidos 
	"""
	return list( client.Links.list(institution__in = empresas) )