print("---MENU DE FILMES---")
print("---  A=  AÇÃO    ---")
print("---  B=  TERROR  ---")
print("---  C=  COMÉDIA ---")
print("---  D=  FICÇÃO  ---")

genero = input("Digite o número correspondente ao filme que deseja:") .upper()

match genero:
        #PODE USAR UPPER OU CASE "TESTE" | "teste"
        case "A" | "a": 
            print("Você escolheu Ação, filme indicado é: John Wick!")

        case "B": 
            print("Você escolheu Terror, filme indicado é: Invocação do mal!")

        case "C": 
            print("Você escolheu Comédia filme indicado é: As branquelas!")
        
        case "D": 
            print("Você escolheu Ficção, filme indicado é: Interstelar!")

        case _:
            print("Escolha inválida, tente novamente com um número válido")