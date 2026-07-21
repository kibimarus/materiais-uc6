from operator import truediv
import random

pontos_player = 0
pontos_cpu = 0

jogada_player = 0
jogada_cpu = 0

vai_sair = 0

while vai_sair == False:
        print("Bem-vindo ao JO-KEN-PO")
        print("="*10)
        print("0- Pedra")
        print("1- Papel")
        print("2- Tesoura")
        print("Sua jogada: ")
Jogada_player = int(input("-> "))
if jogada_player < 0 or jogada_player > 2:
    print("Jogada Inexistente!")
    input("Pressione enter para continuar... ")

    print("#"*20)
    print("#"*20)

    jogada_cpu = random.radiant(0,2)

    nome_jogada_player = ""
    nome_jogada_cpu = ""

    match jogada_player:
        case 0:
            nome_jogada_player = "Pedra"
        case 1:
            nome_jogada_player = "Papel"
        case 2:
            nome_jogada_player = "Tesoura"

    match jogada_cpu:
        case 0:
            nome_jogada_cpu = "Pedra"
        case 1:
            nome_jogada_player = "Papel"
        case 2:
            nome_jogada_player = "Tesoura"

    print("A máquina jogou: ", nome_jogada_cpu)          
    print("Você jogou : ", nome_jogada_player)

    if jogada_player ==0 and jogada_cpu==2:
        print("Você venceu!")
        pontos_player = pontos_player + 1
    elif jogada_player ==1 and jogada_cpu == 2:
        print("Você venceu!")
        pontos_player = pontos_player + 1 
    elif jogada_player == 2 and jogada_cpu == 1:
        print("Você venceu!")
        pontos_player = pontos_player +1
    elif jogada_player ==  2 and jogada_cpu == 0:
        print("Você perdeu!")
        pontos_cpu = pontos_cpu + 1
    elif jogada_player == 0 and jogada_cpu == 1:
        print("Você perdeu!")
        pontos_cpu = pontos_cpu +1
    elif jogada_player == 1 and jogada_cpu == 2:
        print("Você perdeu!")
        pontos_cpu = pontos_cpu + 1
    elif jogada_player == jogada_cpu:
        print("Empatou!")
    input("Pressione enter para continuar... ")
    print("Placar: ")
    print("-"*10)
    print("Player: ", pontos_player)
    print("Maquina: ", pontos_cpu)

    resposta = input("Quer jogar mais uma? s/n \n-> ").upper()
    if resposta != "S": 
        vai_sair = True
print("fim do jogo")