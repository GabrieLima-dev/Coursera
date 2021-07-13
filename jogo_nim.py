def main(x):
    while True:
        if x == 1:
            print("Você escolheu uma partida Isolada!")
            break
        if x == 2:
            print("Voce escolheu um campeonato!")
            break
        if x != 1 or x != 2:
            print("Essa opção não é válida!")
            x = int(input(
                "Bem-vindo ao jogo do NIM! Escolha: \n \n 1 - para jogar uma partida isolada \n 2 - para jogar um campeonato "))


x = int(input("Bem-vindo ao jogo do NIM! Escolha: \n \n 1 - para jogar uma partida isolada \n 2 - para jogar um campeonato "))
print("")
main(x)
