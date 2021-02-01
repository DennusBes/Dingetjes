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
def count(lst, getal):
    count=0
    for i in lst:
        if getal ==i:
            count += 1
    return count
lijstje= [1,1,1,1,1,3,4,5,6,7,8,8,9]
print(count(lijstje, 8 ))



#          OPDRACHT 4
def paling(woord):
    return woord == woord[::-1]

#          OPDRACHT 10
#def fib(n,v0=0, v1=1):
#    return fib_3(n-1 ,v1 v0+v1) if n>1 else (v0, v1) [n]