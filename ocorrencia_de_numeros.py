# sistema de ocorrência de números/ usuário digita um numero da lista e o programa deve responder quantas vezes ele aparece
lista = [1, 3, 5, 3, 7, 9, 3]
print("_"*35)
print("Sistema de Ocorrência de números")
print("-"*35)
print("Lista de Números: ")
print("1, 3, 5, 3, 7, 9, 3")
print("-"*35)

ne = input("Digite o número escolhido: ")
# ne= Número Escolhido

match ne:
    case '1':
        print("Número de ocorrências do número", ne, "na lista: 1")

    case '3':
        print("Número de ocorrências do número", ne, "na lista:3")

    case '5':
        print("Número de ocorrências do número", ne, "na lista: 1")

    case '9':
        print("Número de ocorrências do número", ne, "na lista: 1")

    case _:
        print("Número de ocorrências do número", ne, "na lista: 0")


    