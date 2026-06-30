from ssl import OP_NO_RENEGOTIATION


print("---DIAS DA SEMANA---")
print("--- 1 = DOMINGO  ---")
print("--- 2 = SEGUNDA  ---")
print("--- 3 = TERÇA    ---")
print("--- 4 = QUARTA   ---")
print("--- 5 = QUINTA   ---")
print("--- 6 = SEXTA    ---")
print("--- 7 = SÁBADO   ---")
print("--------------------")


dia = int(input("digite o dia da semana, 1,2,3,4,5,6 ou 7: "))



match dia:

    case 1:
        print("Domingo")

    case 2: 
        print("Segunda-feira")
         
    case 3: 
        print("Terça-feira")

    case 4:
        print("Quarta-feira")

    case 5:
        print("Quinta-feira")

    case 6:
        print("Sexta-feira")

    case 7:
        print("Sábado")

    case _:
        print("Dia inválido, tente novamente com alguma das opções estabelecidas")
