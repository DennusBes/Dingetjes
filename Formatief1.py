#          OPDRACHT 1

# FOR LOOPS
def opdracht1forloop():
    pyramide_size = int(input("Hoe groot? "))
    for i in range(1,pyramide_size):
        print(f'{"*"*i}')
    for i in range(pyramide_size, 0, -1):
        print(f'{"*" * i}')

# WHILE LOOPS
def opdracht1whileloop():
    pyramide_size = int(input("Hoe groot? "))
    pyramide_counter = 1
    while pyramide_counter < pyramide_size:
        print(f'{"*" * pyramide_counter}')
        pyramide_counter += 1
    while pyramide_counter > 0:
        print(f'{"*" * pyramide_counter}')
        pyramide_counter -= 1

# ANDERE KANT
def inversepyramide():
    pyramide_size = int(input("Hoe groot? "))
    for i in range(pyramide_size, 0, -1):
        print(f'{"*" * i}')
    for i in range(1,pyramide_size+1):
        print(f'{"*"*i}')

#          OPDRACHT 2
def zoekdeverschillen():
    text1 = (input("Voer text 1 in: "))
    text2 = (input("Voer text 2 in: "))
    if (len(text1)) > (len(text1)):
        kortste_text = text2
        langste_text = text1
    else:
        kortste_text = text1
        langste_text = text2
    for i in range(len(kortste_text)):
        if kortste_text[i]!=langste_text[i]:
            return print(f'Er vind een verschil plaats op index {i}.')
        else:
            return print(f'Er vind een verschil plaats op index {len(kortste_text)}.')

#          OPDRACHT 3
#  count
def count(lst, getal):
    count=0
    for i in lst:
        if getal ==i:
            count += 1
    return count
lijstje= [1,1,1,1,1,3,4,5,6,7,8,8,9]
#print(count(lijstje, 8 ))

#  verschill
def verschillen(lst):
    diff = 0
    for i in range(0,len(lst)-1):

        if lst[i+1]-lst[i] > diff:
            diff = lst[i+1]-lst[i]
    return diff
#print(verschillen([1,2,8,3,900000000000,5,33,44,55,666]))

#  0 en 1 checker
def listchecker(lst):
    return count(lst,1) > count(lst,0) and count(lst,0) <= 12
#print(listchecker([1,1,1,1,1,1,1,0,0,0,0,0,0]))


#          OPDRACHT 4
def paling(woord):
    return woord == woord[::-1]

#          OPDRACHT 5
def sorting(lst):
    data = lst
    if len(data) > 1:

        middel = len(data)//2
        Left = data[:middel]
        Right = data[middel:]

        mergeSort(Left, sort_value)
        mergeSort(Right, sort_value)

        z = x = c = 0

        while z < len(Left) and x < len(Right):
            if Left[z].get(sort_value) < Right[x].get(sort_value):
                data[c] = Left[z]
                z += 1
            elif Left[z].get(sort_value) == Right[x].get(sort_value):
                if Left[z].get("name") < Right[x].get("name"):
                    data[c] = Left[z]
                    z += 1
                else:
                    data[c] = Right[x]
                    x += 1
            else:
                data[c] = Right[x]
                x += 1
            c += 1

        while z < len(Left):
            data[c] = Left[z]
            z += 1
            c += 1

        while x < len(Right):
            data[c] = Right[x]
            x += 1
            c += 1
    return data

#          OPDRACHT 6
def gemiddelde(lst):
    tot = 0
    for i in lst:
        tot = tot+i
    gem=tot / len(lst)
    return gem



#          OPDRACHT 10
#def fib(n,v0=0, v1=1):
#    return fib_3(n-1 ,v1 v0+v1) if n>1 else (v0, v1) [n]