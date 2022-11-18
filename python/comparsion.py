from process import *

def busca():
    word = words()
    lista = get_path()    
    x = -1
    found = []
    
    for i in lista:
        for j in word:
            x = i.find(j)
            if x != -1: found.append(i[i.index(j)])

    print(found)
    k = NULL

    if k != 0:
        print(result(0))
    else: 
        print(result(1))
    for i in lista:
        print(i)
        
def verificador(value):
    if value > 0:
        return "estudante"
    else: return "nao estudante"
    
busca()