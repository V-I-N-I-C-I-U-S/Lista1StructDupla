import time

nome = ["V","I","N","I","C","I","U","S"]

def mostranome(index):
    for i in range(index):
        print(nome[i],end='')
        time.sleep(0.05)
    print()
    if index > 7:
        desmostranome(7)
        return 0
    else:
        mostranome(index+1)
        
def desmostranome(index):
    for i in range(index):
        print(nome[i],end='')
        time.sleep(0.05)
    print()
    if index <= 0:
        return 0
    else:
        desmostranome(index-1)

while True:
    mostranome(0)
