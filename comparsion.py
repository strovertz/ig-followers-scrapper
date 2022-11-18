from process import *

search_this = ["Analista", "Sistemas", "UFSM"]


x = -1
found = []

for i in lista:
    for j in search_this:
        x = i.find(j)
        if x != -1: found.append(i[i.index(j)])

print(found)
k = NULL

if k != 0:
    print("Estudante da UFSM")
else: 
    print("Nao Estuda na UFSM")

for i in lista:
    print(i)
