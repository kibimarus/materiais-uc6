print("|-- STATUS DO PEDIDO --|")
print("|--  novo/pendente     |") 
print("|--       Pago         |")
print("|--     enviado        |")
print("|--     entregue       |")

genero = input("Digite o Status do seu pedido: ") .upper()

match genero:
        #PODE USAR UPPER OU CASE "TESTE" | "teste"
        case "PENDENTE" | "NOVO": 
            print("Seu pedido está aguardando pagamento")

        case "PAGO": 
            print("Pagamento confirmado! Preparando envio")

        case "ENVIADO": 
            print("Seu pedido já está a caminho!")

        case "ENTREGUE":
            print("Pedido finalizado")
        case _:
            print("Escolha inválida, tente novamente com uma opção válida")
           