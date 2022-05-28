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
        # print(f"i {i} {len(line)} line {l} {line}")
        if(i == '1'):
            colored += 1
    if(D == 0):
        change = colored
        return change
    if(D == 1):
        # print(f"colored {colored}")
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

# print(opt_dist('0000000001', 1))
# print(opt_dist('0000000010', 1))
# print(opt_dist('1000000000', 1))
# print(opt_dist('0100000000', 1))
# 
# print("\n")
# 
# print(opt_dist('0010001000', 5))
# print(opt_dist('0010001000', 4))
# print(opt_dist('0010001000', 3))
# print(opt_dist('0010001000', 2))
# print(opt_dist('0010001000', 1))
# print(opt_dist('0010001000', 0))
# print(opt_dist('0010101000', 5))
# print(opt_dist('0010101000', 4))
# print(opt_dist('0010101000', 3))
# print(opt_dist('0010101000', 2))
# print(opt_dist('0010101000', 1))
# print(opt_dist('0010101000', 0))

# 0
# 0
# 0
# 0

# 3
# 4
# 3
# 2
# 1
# 2
# 2
# 3
# 2
# 3
# 2
# 3

#print("")
#now = datetime.datetime.now() - start
#print(now.microseconds)