
print('Функция 1:')
def hello():
    print('Hello,')
    print('World!')
#Конец определения функции 1.
hello()#Вызов функции 1
#Определение функции 2:
def funcname(x):
    print('Квадрат числа',x,'=',x^2)
#Конец определения функции 2.
funcname(5)#Вызов функции 2, указывая чем является X
print('Функция 2:')
for i in range (1,20):#As many times, as it takes
    funcname(i)
print('Функция 3:')
def arg2(a,b):
    print(a*b)
arg2(10,20)
print('Функция 4:')
def even(t):
    if t%2==0:
        print(t,'Четное')
    else:
        print(t,'Не четное')
for c in range (10,20):
    even(c)
print('Функция 5')
def fkl(n):
    p=1 #Накопление произведения
    for i in range(2,n+1):
        p=p*i
    print(p)
fkl(7)