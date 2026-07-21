import locale
from datetime import date
from ast import If
from smtplib import quoteaddr
locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil')
 
# 2. Obter a data de hoje
data_hoje = date.today()
 
# 3. Formatar a data para obter o nome do dia da semana em português
# %A retorna o nome completo do dia da semana (ex: "Quinta-feira")
dia_da_semana = data_hoje.strftime('%A')

continuar = "SIM"
while continuar == "SIM":

    print("             Bem-vindo ao Cinemark              ")
    print("----------------- Menu de  Filmes----------------")
    print("| Código  |         Nome             |      Gênero     |")
    print("| D039    |   O Poderoso Chefão      |Mafia            |")
    print("| B678    |        Matrix            |Ação             |")
    print("| D889    |   O Senhor dos Anéis     |Fantasia         |")
    print("| M912    |      Interestelar        |Ficção Científica|")
    print("| G007    |O resgate do soldado Ryan |Guerra           |")
    print("_"*50)
    filme = input("Digite o código do filme que deseja assistir: ").upper()

    match filme:

        case"D039":
            filme_escolhido = ("O Poderoso Chefão")

        case"B678":
            filme_escolhido = ("Matrix")
            
        case"D889":
            filme_escolhido = ("O Senhor dos Anéis")

        case"M912":
            filme_escolhido = ("Interestelar")

        case"G007":
            filme_escolhido = ("O resgate do soldado Ryan")

        case _:
            print("CÓDIGO INVÁLIDO ")

    print("o filme escolhido foi: ", filme_escolhido)

    qtd_ingresso = (float(input("Agora escolha a quantidade: ")))

    print("Quantidade escolhida: ", qtd_ingresso)

    if dia_da_semana == "segunda-feira" or dia_da_semana == "quarta-feira" or dia_da_semana == "sexta-feira":
        valor_ingresso = 32.50
    elif dia_da_semana == "terça-feira" or dia_da_semana == "quinta-feira" or dia_da_semana == "sábado" or dia_da_semana =="domingo":
         valor_ingresso = 36.00

    print("o valor no dia é: " , valor_ingresso)

    print("\n"*50)
    print("-------------------------------COMBOS-------------------------------")
    print("| Código |                      Combo                    |   Valor |")
    print("|  005   | Doritos + refri lata                          | R$ 15,90|")
    print("|  072   | Pipoca Salgada + Copo  de  Coca Cola          | R$ 17,90|")
    print("|  777   | Pipoca Doce    + Copo de Suco                 | R$ 14,90|")
    print("|  215   | Refil de Pipoca Salgada + 2 Recargas de refri | R$ 25,00|")
    print("|  000   | NENHUM COMBO           ")

    combo = input("Digite o código correspondente ao combo que deseja: ")

    match combo:
            
        case"005":
            combo_valor = 15.90
            combo_escolhido = ("Doritos + refri lata") 
            
        case"072":
            combo_escolhido =  ("Pipoca Salgada + Copo  de  Coca Cola")
            combo_valor = 17.90

        case"777":
            combo_escolhido = ("Pipoca Doce    + Copo de Suco")
            combo_valor = 14.90

        case"215":
            combo_escolhido = ("Refil de Pipoca Salgada + 2 Recargas de refri")
            combo_valor = 25.00

        case"000":
            combo_escolhido = ("Sem combo") 
            combo_valor = 00.00

        case _:
            print("CÓDIGO INVÁLIDO ")

    qtd_combo = (int(input("Agora a quantidade de combos que deseja: ")))

    valor_ingresso_f = valor_ingresso*qtd_ingresso
    valor_combof = combo_valor*qtd_combo
    total = valor_ingresso_f + valor_combof
 
    print("\n"*50)
    print("-----------------------------------Resumo da compra--------------------------")
    print(  qtd_ingresso, "ingresso(s) para ", filme_escolhido, "= R$ ", valor_ingresso_f )
    print( qtd_combo, combo_escolhido, " = R$" , valor_combof                              )
    print("Total da compra: = R$ ", total )

    continuar = input("Deseja fazer outra compra? (Sim/não): ") .upper()
    
print("Obrigado pela preferência!")




