




n= int(input("Array size XY:"))
check = 0
N = []

for i in range(n):
    N =[]         #ЗАПОМНИ: 2 for, потому что он делает n строк с n чисел
    for j in range(n):
        N.append(int(input("Array numbers: ")))  #Создание массива 
#for i in N:
 #   print(i)



for i in range(n):
    for j in range(n):
        if N[i][j] != N[j][i]:    # Проверка на симметричность
            check=+ 1
            


if check > 0:
    print('No')    #Ответ:
else:
    print('Yes')