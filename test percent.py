connect = True

while connect == True:
    number = input('Число: ')
    procent = input('Процент: ')
    while type(number) != int:
        try:
              number = int(number)
              procent = int(procent)
        except ValueError:
             print('Вводи нормальные значения!')
             number = input('Число: ')
             print()
             procent = input('Процент: ')
             print()
    while type(number) != float:
        try:
              number = float(number)
              procent = float(procent)
        except ValueError:
             print('Вводи нормальные значения!')
             number = input('Число: ')
             print()
             procent = input('Процент: ')
             print()
    
    finish = number /100 * procent
    print('Ответ:', float(finish))