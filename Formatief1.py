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

#          OPDRACHT 2
def zoekdeverschillen():
    text1 = (input("Voer text 1 in: "))
    text2 = (input("Voer text 2 in: "))
    if (len(text1)) > (len(text1)):
        kortste_text = text2
    else:
        kortste_text = text1
    for i in range(len(kortste_text)):
        if text1[i]!=text2[i]:
            print(f'Er vind een verschil plaats op index {i}.')

zoekdeverschillen()