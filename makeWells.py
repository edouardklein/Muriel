#!env python3
import json

wellList = []

print("Liste des postes de dépense")

while True: #Do... while loop
    wellName = input("Dépense : ")
    if not wellName:
        break
    wellAmount = int(input("Montant (en centimes) : "))
    wellList.append([wellName,wellAmount])
    
with open('wells.list', mode='w', encoding='utf-8') as f:
    json.dump(wellList, f, indent=2)



