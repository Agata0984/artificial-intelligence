import datetime
start = datetime.datetime.now()

def opt_dist(line, D):
    l = len(line)
    change = 0
    colored = 0
    arr = []
    temp1 = 0
    temp2 = D
    for i in line:
        if(i == '1'):
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
        if(line[i] == '1'):
            temp1 += 1
    arr.append(temp1)
    for i in range(l-D):
        if(line[temp2] == '1'):
            temp1 += 1
        if(line[temp2 - D] == '1'):
            temp1 -= 1
        temp2 +=1
        arr.append(temp1)
    max = 0
    for i in range(l-D+1):
        if(arr[i]>max):
            max = arr[i]
    change = D - max + colored - max
    return change

file2 = open("zad4_input.txt", "r") 
file1 = open("zad4_output.txt", "w") 
for i in file2:
    array = i.split(" ")
    print(int(array[1]))
    file1.write(str(opt_dist(array[0], int(array[1]))) + "\n")
file1.close()
