seq = []
while True:
    i = int(input("Digite um número: "))
    if i == 0:
        break
    seq.append(i)

for i in reversed(seq):
    print(i)