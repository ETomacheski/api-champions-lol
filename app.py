from flask import Flask, request, jsonify
import utils_lol  # type: ignore # Adjust the import based on the actual content of utils-lol.py
app = Flask(__name__)

#Base de dados com países
COUNTRIES = [
    {'id':1,'name':'Brasil', 'capital': 'Brasilia'},
    {'id':2,'name':'Estados Unidos', 'capital': 'Washington' },
    {'id':3,'name':'Argentina', 'capital': 'Buenos Aires' }
]
max_id = 3

# Busca todos os campeões
@app.get("/champions")
def getChampions():
    return utils_lol.getChampions(), 200

#Busca um campeão pelo nome
@app.get("/champions/<string:name>")
def getChampionsName(name):
    champion = utils_lol.getChampionByName(name)
    if champion is not None:
        return champion, 200
    return {"erro": "Campeão não encontrado"}, 404

@app.post("/champions")
def addChampions():
    if request.is_json:
        champion = request.get_json()
        response = utils_lol.addChampion(champion)
        if 'erro' in response:
            return response, 400
        return response, 201
    return {"erro":"Formato deve ser JSON"}, 415

@app.put("/champions/<string:name>")
def updateChampions(name):
    if request.is_json:
        champion = request.get_json()
        response = utils_lol.updateChampion(name, champion)
        if 'erro' in response:
            return response, 400
        return response, 201
    return {"erro":"Formato deve ser JSON"}, 415

#Remove campeão pelo nome passado como variável na URL
@app.delete("/champions/<string:name>")
def deleteChampion(name):
    response = utils_lol.deleteChampion(name)
    if 'erro' in response:
        return response, 404
    return response, 200