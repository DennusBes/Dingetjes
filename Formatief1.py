#          OPDRACHT 1
# FOR LOOPS
pyramide_size = int(input("Hoe groot? "))
for i in range(1,pyramide_size):
    print(f'{"*"*i}')
for i in range(pyramide_size, 0, -1):
    print(f'{"*" * i}')
# WHILE LOOPS
pyramide_counter = 1
while pyramide_counter < pyramide_size:
    print(f'{"*" * pyramide_counter}')
    pyramide_counter += 1
while pyramide_counter > 0:
    print(f'{"*" * pyramide_counter}')
    pyramide_counter -= 1

