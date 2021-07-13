tipo_jogo = 0


def computador_escolhe_jogada(n, m):

    print("Vez do computador!")
    if n <= m:
        return n

    else:
        quantia = n % (m+1)
        if quantia > 0:
            return quantia

        return m


def usuario_escolhe_jogada(n, m):

    print("Sua vez!\n")
    jogada = 0

    while jogada == 0:
        jogada = int(input("Quantas peças irá tirar? "))

        if jogada > n or jogada < 1 or jogada > m:
            jogada = 0

    return jogada


def partida():

    print(" ")
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    is_computer_turn = True

    if n % (m+1) == 0:
        is_computer_turn = False
    while n > 0:

        if is_computer_turn:
            jogada = computador_escolhe_jogada(n, m)
            is_computer_turn = False
            print("Computador retirou {} peças.".format(jogada))
        else:
            jogada = usuario_escolhe_jogada(n, m)
            is_computer_turn = True
            print("Você retirou {} peças.".format(jogada))

        n = n - jogada

        print("Restam apenas {} peças em jogo.\n".format(n))

    if is_computer_turn:
        print("Você ganhou!")
        return 1
    else:
        print("O computador ganhou!")
        return 0


def campeonato():

    usuario = 0
    computador = 0

    for _ in range(3):

        vencedor = partida()

        if vencedor == 1:
            usuario = usuario + 1
        else:
            computador = computador + 1

    print("Placar final: Você  {} x {}  Computador".format(usuario, computador))


def main(x):
    while True:
        if x == 1:
            print("Você escolheu uma partida Isolada!")
            partida()
            break
        if x == 2:
            print("Voce escolheu um campeonato!")
            campeonato()
            break
        if x != 1 or x != 2:
            print("Essa opção não é válida!")
            x = int(input(
                "Bem-vindo ao jogo do NIM! Escolha: \n \n 1 - para jogar uma partida isolada \n 2 - para jogar um campeonato "))


x = int(input("Bem-vindo ao jogo do NIM! Escolha: \n \n 1 - para jogar uma partida isolada \n 2 - para jogar um campeonato "))
print("")
main(x)
