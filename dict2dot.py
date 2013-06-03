#!env python3
import json
import sys

with open(sys.argv[1], mode='r', encoding='utf-8') as f:
    Dict = json.load(f)

with open('actors.list', mode='r', encoding='utf-8') as f:
    actorList = json.load(f)

with open('wells.list', mode='r', encoding='utf-8') as f:
    wellList = json.load(f)
print(r'digraph G { overlap="false"')
for actor in actorList:
    print(str(abs(hash(actor)))+" [label=\"{}\"];".format(actor))
for well in wellList:
    print(str(abs(hash(well[0])))+r' [label="{}\n{:.2f}",shape=box,style=filled,fillcolor="grey"];'.format(well[0],well[1]/100.))
    
for k in Dict:
    for v in Dict[k]:
        src = str(abs(hash(k)))
        dst = str(abs(hash(v[0])))
        weight = "{:.2f}".format(v[1]/100.)
        print('{} -> {} [label={},fontcolor="blue"];'.format(src,dst,weight))
print("}")
