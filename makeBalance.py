#!env python3
import json

BOLD='\033[1m'
ENDBOLD='\033[0m'

with open('real.dict', mode='r', encoding='utf-8') as f:
    d_real = json.load(f)
    
with open('ideal.dict', mode='r', encoding='utf-8') as f:
    d_ideal = json.load(f)

with open('actors.list', mode='r', encoding='utf-8') as f:
    actorList = json.load(f)


d_balance = {}
print(BOLD+'Name             Ideal            Real             Balance'+ENDBOLD)
for actor in actorList:
    idealExpenses = sum(a[1] for a in d_ideal[actor])
    realExpenses = sum(a[1] for a in d_real[actor])
    diff = idealExpenses - realExpenses
    print('{name:<16} {ideal:<16.2f} {real:<16.2f} {diff:<16.2f}'
          .format(name=actor,
                  real=realExpenses/100.,
                  ideal=idealExpenses/100.,
                  diff=diff/100.))
    d_balance[actor] = [idealExpenses,realExpenses,diff]
print(BOLD+"Total            "+ENDBOLD+'{:<16.2f} {:<16.2f} {:<16.2f}'
      .format(sum(a[0] for a in d_balance.values())/100.,
              sum(a[1] for a in d_balance.values())/100.,
              sum(a[2] for a in d_balance.values())/100.))
assert( abs(sum(a[0] for a in d_balance.values()) - sum(a[1] for a in d_balance.values())) < 1e-5 ) #Sum of ideal expenses is the same as sum of real expenses at float precision
assert( abs(sum(a[2] for a in d_balance.values())) < 1e-5 ) #Sum of diffs is 0 at float precision

suckers = [a for a in actorList if d_balance[a][2] < 0]
fuckers = [a for a in actorList if d_balance[a][2] > 0]
totalSuckers = sum(d_balance[a][2] for a in suckers)
totalFuckers = sum(d_balance[a][2] for a in fuckers)

print()
print(BOLD+"Fuckers                         Suckers"+ENDBOLD)
while len(suckers) > 0 or len(fuckers) > 0:
    try:
        s = suckers.pop()
        s_sAmount = '{:.2f}'.format(d_balance[s][2]/100.)
    except IndexError:
        s = ''
        s_sAmount = ''
    try:
        f = fuckers.pop()
        s_fAmount = '{:.2f}'.format(d_balance[f][2]/100.)
    except IndexError:
        f = '                '
        s_fAmount = '                '
    print('{:<16}{:<16}{:<16}{:<16}'
          .format(f,s_fAmount,s,s_sAmount))
print((BOLD+'{:<16}'+ENDBOLD+'{:<16.2f}{:<16}{:<16.2f}')
      .format('Total',
              totalFuckers/100.,
              '',
              totalSuckers/100.))


