x = int(input("Digite os números:"))
while x >= 0:
    y = 1
    while x >= 1:
        y *= x
        x -= 1
        x = int(input("Digite os números:"))
        print(y)
