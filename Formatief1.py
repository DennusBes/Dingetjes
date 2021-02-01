#          OPDRACHT 1

pyramide_size = int(input("Hoe groot? "))
for i in range(1,pyramide_size):
    print(f'{"*"*i}')
for i in range(pyramide_size, 0,-1):
    print(f'{"*" * i}')

    