#!env python3
import json

actorList = []

actor = input("Liste des acteurs :")
while actor:
    actorList.append(actor)
    actor = input()
    
with open('actors.list', mode='w', encoding='utf-8') as f:
    json.dump(actorList, f, indent=2)



