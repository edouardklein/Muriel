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
    print('Entrez (en centimes) la participation des différents acteurs pour le poste de dépense '+
           BOLD+wellName+ENDBOLD+
           ' pour un montant total de '+
           BOLD+"{:.2f}".format(wellAmount/100.)+ENDBOLD)
    total = 0
    for actor in actorList:
        str_amount = input(actor+" : ")
        if str_amount:
            amount = int(str_amount)
            graph[actor].append([wellName,amount])
            total += amount
    assert(total == wellAmount)

with open('real.dict', mode='w', encoding='utf-8') as f:
    json.dump(graph, f, indent=2)

