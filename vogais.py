def vogal(x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u" or x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
        return True
    else:
        return False


n = input("Digite uma letra: ")
print(vogal(n))
