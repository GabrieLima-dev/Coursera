n = int(input("Digite um numero: "))
count = 0

while n != 0:
    s = n % 10
    n = n // 10
    count += s
print(count)