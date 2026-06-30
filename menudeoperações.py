string = input("Digite o número da String de 0 a 9: ") .upper()

match string: 
    case "1"|"2"|"3":
        print("Carregando o jogo...")

    case "8"|"9":
        print("Abrindo configurações...")
    
    case "0"|"SAIR":
        print("Saindo do sistema...")

    case _: 
        print("Opção indisponível, tente novamento com um número válido!")





