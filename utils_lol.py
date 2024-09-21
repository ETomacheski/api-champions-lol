import json

def getChampions():
    with open('champions.json', 'r') as arquivo:
        champions = json.load(arquivo)
    return champions

def getChampionByName(name):
    with open('champions.json', 'r') as arquivo:
        champions = json.load(arquivo)
    
    champions_filtered = next(filter(lambda champion: champion['Name'] == name, champions), None)

    
    if champions_filtered is None:
        return None
    return champions_filtered

mandatoryFields = ['Name', 'Tags', 'Role', 'Range type', 'Resourse type', 'Base HP', 'HP per lvl', 
 'Base mana', 'Mana per lvl', 'Movement speed', 'Base armor', 'Armor per lvl', 
 'Base magic resistance', 'Magic resistance per lvl', 'Attack range', 
 'HP regeneration', 'HP regeneration per lvl', 'Mana regeneration', 
 'Mana regeneration per lvl', 'Attack damage', 'Attack damage per lvl', 
 'Attack speed per lvl', 'Attack speed', 'AS ratio']

def addChampion(champion):
    notFoundMandatoryFields = []
    
    for field in mandatoryFields:
        if field not in champion:
            notFoundMandatoryFields.append(field)
    if len(notFoundMandatoryFields) > 0:
        return {"erro": f"Campeão não possui os campos obrigatórios: {notFoundMandatoryFields}"}
    
    existsChampion = getChampionByName(champion['Name'])
    if existsChampion is not None:
        return {"erro": "Campeão já cadastrado"}
    
    with open('champions.json', 'r') as arquivo:
        champions = json.load(arquivo)
    
    champions.append(champion)
    
    with open('champions.json', 'w') as arquivo:
        json.dump(champions, arquivo, indent=4)
    
    return champion

def deleteChampion(name):
    with open('champions.json', 'r') as arquivo:
        champions = json.load(arquivo)
    
    champion = next(filter(lambda champion: champion['Name'] == name, champions), None)
    
    if champion is None:
        return {"erro": "Campeão não encontrado"}
    
    champions.remove(champion)
    
    with open('champions.json', 'w') as arquivo:
        json.dump(champions, arquivo, indent=4)
    
    return champion

def updateChampion (name, champion):
    with open('champions.json', 'r') as arquivo:
        champions = json.load(arquivo)
    
    championToUpdate = next(filter(lambda champion: champion['Name'] == name, champions), None)
    
    if championToUpdate is None:
        return {"erro": "Campeão não encontrado"}
    
    if('Name' in champion):
        return {"erro": "Não é possível alterar o nome do campeão"}	
    
    championToUpdate.update(champion)
    
    with open('champions.json', 'w') as arquivo:
        json.dump(champions, arquivo, indent=4)
    
    return championToUpdate