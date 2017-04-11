import random
num=random.randint(1,50)
for n in range(1,num):
    if n%5==0:
        print(n,"es múltiplo de 5")
else:
    print("No hay más múltiplos de 5 en la lista")

    