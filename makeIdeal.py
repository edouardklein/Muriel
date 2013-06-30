#!env python3
import json

BOLD='\033[1m'
ENDBOLD='\033[0m'

with open('wells.list', mode='r', encoding='utf-8') as f:
    wellList = json.load(f)
    
with open('actors.list', mode='r', encoding='utf-8') as f:
    actorList = json.load(f)

try:
    f = open('ideal.dict','r',encoding='utf-8')
    existingGraph = json.load(f)
except FileNotFoundError:
    existingGraph = {}
    
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
        try:
            actorAndWell = [a for a in existingGraph[actor] if a[0] == wellName]
            assert( len(actorAndWell)==0 or len(actorAndWell) == 1)
            if len(actorAndWell) == 0:
                raise Exception("Basically a goto to the except block")
            defaultAmount = (actorAndWell[0])[2]
        except (Exception,KeyError):
            defaultAmount = 0
        str_amount = input(actor+" : ["+str(defaultAmount)+"]")
        if str_amount or defaultAmount:
            amount = float(str_amount) if str_amount else defaultAmount
            partGraph[actor] = amount
            total += amount
    for actor in partGraph:
        graph[actor].append([wellName,
                             partGraph[actor]/total*wellAmount,
                             partGraph[actor]])

with open('ideal.dict', mode='w', encoding='utf-8') as f:
    json.dump(graph, f, indent=2)

