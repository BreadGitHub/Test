import random
print('Randomizer')
connect = True
while connect == True:
    a = input('От: ')
    b = input('До: ')
    finish = random.randint(int(a),int(b))
    print('Ответ:', int(finish))
input()