
def calculando_desconto(preco):
    valord = preco * desconto /100
    final = preco - valord
    print("------Resumo da compra------")
    print("Preço original do produto: ", preco, "R$")
    print("Desconto: ", desconto,"%")
    print("O Valor do desconto em reais: ", valord,"R$")
    print("Preço final: ",final,"R$")

preco = float (input("Digite o preço do produto: "))
desconto = float (input("Digite a porcentagem de desconto: "))
calculando_desconto(preco)

