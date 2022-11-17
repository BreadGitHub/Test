
def test(x):
    x = int(input("Number:"))
    if x % 2 != 0:
        print(x)
    else:
        test(x)
x = 0
test(x)