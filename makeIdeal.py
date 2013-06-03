#!env python3
import json

BOLD='\033[1m'
ENDBOLD='\033[0m'

with open('wells.list', mode='r', encoding='utf-8') as f:
    wellList = json.load(f)
    
with open('actors.list', mode='r', encoding='utf-8') as f:
    actorList = json.load(f)


graph = {}

for actor in actorList:
    graph[actor] = []

for well in wellList:
    wellName = well[0]
    wellAmount = well[1]
    graph[wellName] = []
    print('Entrez le nombre de parts des différents acteurs pour le poste de dépense '+
           BOLD+wellName+ENDBOLD)
    total = 0.
    partGraph = {}
    for actor in actorList:
        str_amount = input(actor+" : ")
        if str_amount:
            amount = float(str_amount)
            partGraph[actor] = amount
            total += amount
    for actor in partGraph:
        graph[actor].append([wellName,
                             partGraph[actor]/total*wellAmount,
                             partGraph[actor]])

with open('ideal.dict', mode='w', encoding='utf-8') as f:
    json.dump(graph, f, indent=2)

