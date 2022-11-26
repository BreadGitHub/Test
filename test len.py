import random
def test1(b1):
    a = []
    c = 0
    for i in range (b1):
        c += 5
        a.append(c)
    for i in range(len(a)):
        print(a[i])
    for i in range(len(a)):  #len считает сколько вообще букв/цифр в массиве
        i += 1
        print(i) #Программа проработала 7 раз, потому что в массиве 7 символов
    return(i)
test1(b1 = int(input("Write the number:")))

