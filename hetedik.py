import Renszarvas
def beolvas():
    lista = []
    befajl = open("fajlok/Mikulasszan.txt", "r", encoding="utf-8")
    adatokListaja = befajl.readlines()
    # print(adatokListaja)
    for index in range(1, len(adatokListaja),1):
        if not ("Santa Claus" in adatokListaja[index]):
            daraboltSor = adatokListaja[index].split("@")
            # print(daraboltSor)
            szarvas = Renszarvas.Renszarvas(daraboltSor[0], daraboltSor[1], daraboltSor[2], daraboltSor[3])
            lista.append(szarvas)
    befajl.close()
    return lista

def hetes():

    szarvasokListaja = beolvas()