#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Создание списка 1
n = int(input("количество списков n:"))
N = [0]*n 
m = int(input("Нулей в списке m:"))
for i in range(n):
    N[i] = [0]*m
print("Первый пример N:", N)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Создание списка 2
K = []
k = 4 #Сколько нулей в каждом списке
t = 3 #Сколько списков
for i in range(t):
    K.append([0]*k)
print("Второй пример K:", K)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Вывод вложенного списка
l = 3
L = []
for i in range(l):
    J = []
    for i in range(l):
        J.append(int(input()))
    L.append(J)
for i in range(l):
    for j in range(l):
        print(L[i][j], end=' ')
        print()