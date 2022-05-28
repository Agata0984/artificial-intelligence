import random

def sortowanie(tab):
    for i in range(5):
        for j in range(i, 5):
            if(tab[0][j]<tab[0][i]):
                temp = tab[0][i]
                tab[0][i] = tab[0][j]
                tab[0][j] = temp
                temp = tab[1][i]
                tab[1][i] = tab[1][j]
                tab[1][j] = temp


def uklady(tab):
    # poker
    if(tab[0][0]+1 == tab[0][1] and tab[0][1]+1 == tab[0][2] and 
       tab[0][2]+1 == tab[0][3] and tab[0][3]+1 == tab[0][4] and 
       tab[1][0] == tab[1][1] and tab[1][0] == tab[1][2] and 
       tab[1][0] == tab[1][3] and tab[1][0] == tab[1][4]):
        return 1
    # kareta
    if(tab[0][0] == tab[0][1] and tab[0][1] == tab[0][2] and 
       tab[0][2] == tab[0][3]):
        return 2
    if(tab[0][1] == tab[0][2] and tab[0][2] == tab[0][3] and 
       tab[0][3] == tab[0][4]):
        return 2
    # full
    if(tab[0][0] == tab[0][1] and tab[0][1] == tab[0][2] and 
       tab[0][3] == tab[0][4]):
        return 3
    if(tab[0][0] == tab[0][1] and tab[0][2] == tab[0][3] and 
       tab[0][3] == tab[0][4]):
        return 3
    # kolor
    if(tab[1][0] == tab[1][1] and tab[1][0] == tab[1][2] and 
       tab[1][0] == tab[1][3] and tab[1][0] == tab[1][4]):
        return 4
    # strit
    if(tab[0][0]+1 == tab[0][1] and tab[0][1]+1 == tab[0][2] and 
       tab[0][2]+1 == tab[0][3] and tab[0][3]+1 == tab[0][4]):
        return 5
    # trojka
    if(tab[0][0] == tab[0][1] and tab[0][1] == tab[0][2]):
        return 6
    if(tab[0][2] == tab[0][3] and tab[0][3] == tab[0][4]):
        return 6
    if(tab[0][1] == tab[0][2] and tab[0][2] == tab[0][3]):
        return 6
    # dwie pary
    if(tab[0][0] == tab[0][1] and tab[0][2] == tab[0][3]):
        return 7
    if(tab[0][0] == tab[0][1] and tab[0][3] == tab[0][4]):
        return 7
    if(tab[0][1] == tab[0][2] and tab[0][3] == tab[0][4]):
        return 7
    # para 
    if(tab[0][0] == tab[0][1] or tab[0][1] == tab[0][2] or 
       tab[0][2] == tab[0][3] or tab[0][3] == tab[0][4]):
        return 8
    # wysoka karta
    return 9





def poker(a, c):
    figury = ["As", "Krol", "Dama", "Walet"]
    blotki = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    figurant = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    blotkarz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    # losowanie

    f = [0, 0, 0, 0, 0]
    b = [0, 0, 0, 0, 0]

    f[0] = int(random.random()*32)%16
    b[0] = int(random.random()*72)%a   # 2,3,4 12, jeden kolor 9
    
    for i in range(1, 5):
        f[i] = int(random.random()*32)%16
        licznik = 0
        for j in range(i):
            if(f[j] == f[i]):
                licznik = 1
        while(licznik == 1):
            f[i] = int(random.random()*32)%16
            licznik = 0
            for j in range(i):
                if(f[j] == f[i]):
                    licznik = 1
        

    for i in range(1, 5):
        b[i] = int(random.random()*72)%a   # 2,3,4 12, jeden kolor 9
        licznik = 0
        for j in range(i):
            if(b[j] == b[i]):
                licznik = 1
        while(licznik == 1):
            b[i] = int(random.random()*72)%a   # 2,3,4 12, jeden kolor 9
            licznik = 0
            for j in range(i):
                if(b[j] == b[i]):
                    licznik = 1

        
    for i in range(5):
        figurant[0][i] = int(f[i]/4) # karta
        figurant[1][i] = int(f[i])%4 # kolor
    
    for i in range(5):
        blotkarz[0][i] = int(b[i]/c) # karta  dla jednego koloru 1
        blotkarz[1][i] = int(b[i])%c # kolor  dla jednego koloru 1
    
    sortowanie(figurant)
    sortowanie(blotkarz)
    
    #for i in range(5):
    #    print(figury[figurant[0][i]])
    #    print(figurant[1][i])
    #for i in range(5):
    #    print(blotki[blotkarz[0][i]])
    #    print(blotkarz[1][i])

    F = uklady(figurant)
    B = uklady(blotkarz)
    if(F == B):
        return 0
    elif(B<F):
        return 1
    else:
        return 0


def prwd(a ,c):
    suma = 0
    for i in range(10000):
        suma += poker(a ,c)

    suma/=100
    print("szanse blotkarza to " + str(suma) + "%")


def test():
    n = int(random.random()*72)%36
    tab = []
    n=0
    for i in range(n):
        tab.append(0)
    #tab[0] = int(random.random()*72)%36
    for i in range(1, n):
        tab[i] = int(random.random()*72)%36
        for j in range(i):
            while(tab[j] == tab[i]):
                tab[i] = int(random.random()*72)%36
        print(str(int(tab[i]/4)+2) + " " + str(tab[i]%4))
    #prwd(tab, n)


print("wszystkie blotki")
prwd(36, 4)
print("2, 3, 4 z kazdego koloru")
prwd(12, 4)
print("tylko jeden kolor")
prwd(9, 1)
print("tylko jeden kolor, 5 pierwszych kart")
prwd(5, 1)