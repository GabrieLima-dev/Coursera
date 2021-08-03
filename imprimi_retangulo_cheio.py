x = int(input("Digite a largura: "))
y = int(input("Digite a altura: "))

linha = 0
coluna = 0

while linha < y:
    while coluna < x:
        print("#", end="")
        coluna = coluna + 1
    print()

    linha = linha+1
    coluna = 0
