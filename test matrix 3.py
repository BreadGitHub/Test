n = int(input("Size XY:"))
b = n*n
for i in range(n):
    N = []
    for i in range(n):
        N.append(int(input("Write the numbers:")))

for i in range(b):
    for j in range(b):
        print(N[i][j], end =' ')


k = 0# счетчик
for i in range(n):
    for j in range(i):             #Проверка симметричности
        if N[i][j] != N[j][i]:
            k +=1


if k > 0:
    print("nope")
else:
    print("Yes")