#!env python3
import json

BOLD='\033[1m'
ENDBOLD='\033[0m'

with open('wells.list', mode='r', encoding='utf-8') as f:
    wellList = json.load(f)
    
with open('actors.list', mode='r', encoding='utf-8') as f:
    actorList = json.load(f)

try:
    f = open('real.dict','r',encoding='utf-8')
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
    print('Entrez (en centimes) la participation des différents acteurs pour le poste de dépense '+
           BOLD+wellName+ENDBOLD+
           ' pour un montant total de '+
           BOLD+"{:.2f}".format(wellAmount/100.)+ENDBOLD)
    total = 0
    for actor in actorList:
        try:
            actorAndWell = [a for a in existingGraph[actor] if a[0] == wellName]
            assert( len(actorAndWell)==0 or len(actorAndWell) == 1)
            defaultAmount = (actorAndWell[0])[1]
        except (IndexError,KeyError):
            defaultAmount = 0
        str_amount = input(actor+" : ["+str(defaultAmount)+"]")
        if str_amount or defaultAmount:
            amount = int(str_amount) if str_amount else defaultAmount 
            graph[actor].append([wellName,amount])
            total += amount
    assert(total == wellAmount)

with open('real.dict', mode='w', encoding='utf-8') as f:
    json.dump(graph, f, indent=2)

