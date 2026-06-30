numero = input("Digite o número, 1 ou 2 : ")

match numero:

    case "1": 
        print("você escolheu o número um!")

    case "2":
        print("Você escolheu o número 2!")

    case _: 
        print("Número inválido, tente novamente com uma das opções!")