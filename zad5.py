import datetime
import random
start = datetime.datetime.now()

def opt_dist(line, D):
    l = len(line)
    change = 0
    colored = 0
    arr = []
    temp1 = 0
    temp2 = D
    for i in line:
        if(i == 1):
            colored += 1
    if(D == 0):
        change = colored
        return change
    if(D == 1):
        if(colored > 0):
            change = colored-1
        else:
            change = 1
        return change
    for i in range(D):
        if(line[i] == 1):
            temp1 += 1
    arr.append(temp1)
    for i in range(l-D):
        if(line[temp2] == 1):
            temp1 += 1
        if(line[temp2 - D] == 1):
            temp1 -= 1
        temp2 +=1
        arr.append(temp1)
    max = 0
    for i in range(l-D+1):
        if(arr[i]>max):
            max = arr[i]
    change = D - max + colored - max
    return change


def check(tab, kol, arr1, arr2, n):
    for i in range(n):
        if(opt_dist(tab[i], arr2[i]) != 0):
            return False
    for i in range(n):
        if(opt_dist(kol[i], arr1[i]) != 0):
            return False
    return True


def draw(tab, n):
    for i in range(n):
        out = ""
        for j in range(n):
            if(tab[i][j] == 1):
                out += '#'
            else:
                out += '.'
        print(out)


def pic(n, arr1, arr2):
    tab = [[0] * n for i in range(n)]
    kol = [[0] * n for i in range(n)]
    licznik = 0

    while(check(tab, kol, arr1, arr2, n) == False):
        wiersz = int(random.random()*100)%n
        while(opt_dist(tab[wiersz], arr2[wiersz])==0):
            licznik +=1
            if(licznik%4==0):
                x = int(random.random()*100)%n
                y = int(random.random()*100)%n
                if(kol[x][y] == 0):
                    tab[y][x] = 1
                    kol[x][y] = 1
                else:
                    tab[y][x] = 0
                    kol[x][y] = 0
            wiersz = int(random.random()*100)%n
        kolumny = []
        for j in range(n):
            kolumny.append(0)
        for j in range(n):
            kolumny[j] = opt_dist(kol[j], arr1[j]) + opt_dist(tab[wiersz], arr2[wiersz])
            #print(kolumny[j])
            if(kol[j][wiersz] == 0):
                kol[j][wiersz] = 1
                tab[wiersz][j] = 1
                #print("dobrze")
            else:
                kol[j][wiersz] = 0
                tab[wiersz][j] = 0
                #print("zle")
            #draw(tab, n)
            kolumny[j] -= (opt_dist(kol[j], arr1[j]) + opt_dist(tab[wiersz], arr2[wiersz]))
            #print(kolumny[j])
            if(kol[j][wiersz] == 0):
                kol[j][wiersz] = 1
                tab[wiersz][j] = 1
            else:
                kol[j][wiersz] = 0
                tab[wiersz][j] = 0
            #print(kolumny[j])
        max = 0
        for j in range(1, n):
            if(kolumny[j]>kolumny[max]):
                max = j
        if(kol[max][wiersz] == 0):
            tab[wiersz][max] = 1
            kol[max][wiersz] = 1
        else:
            tab[wiersz][max] = 0
            kol[max][wiersz] = 0
        
    draw(kol, n)



arr1 = [7, 7, 7, 7, 7, 7, 7]
arr2 = [7, 7, 7, 7, 7, 7, 7]

pic(7, arr1, arr2)
print("")

arr1 = [7, 6, 5, 4, 3, 2, 1]
arr2 = [1, 2, 3, 4, 5, 6, 7]

pic(7, arr1, arr2)
print("")

arr1 = [2, 2, 7, 7, 2, 2, 2]
arr2 = [4, 4, 2, 2, 2, 5, 5]

pic(7, arr1, arr2)
print("")

arr1 = [2,2, 7, 7, 2, 2, 2]
arr2 = [2, 2, 7, 7, 2, 2, 2]

pic(7, arr1, arr2)
print("")

arr1 = [7, 5, 3, 1, 1, 1, 1]
arr2 = [1, 2, 3, 7, 3, 2, 1]

pic(7, arr1, arr2)
print("")

arr1 = [0, 0, 0, 0, 0, 0, 0]
arr2 = [0, 0, 0, 0, 0, 0, 0]

pic(7, arr1, arr2)
print("")

now = datetime.datetime.now() - start
print(now.seconds)



        #######
        #######
        #######
        #######
        #######
        #######
        #######


#       #######
#       .######
#       ..#####
#       ...####
#       ....###
#       .....##
#       ......#

#       ##.....
#       ##.....
#       #######
#       #######
#       .....##
#       .....##
#       .....##

#       ..##...
#       ..##...
#       #######
#       #######
#       ..##...
#       ..##...
#       ..##...

#       #######
#       .#####.
#       ..###..
#       ...#...
#       ...#...
#       ...#...
#       ...#...

#       .......
#       .......
#       .......
#       .......
#       .......
#       .......
#       .......