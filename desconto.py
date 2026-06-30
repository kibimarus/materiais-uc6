from ast import If


print("---Bem-vindo---")
idade = int(input("para começar digite sua idade: "))
vc = float(input("agora digite o valor da compra: R$ "))

if idade < 12:
    categoria =  "Criança"
elif idade <= 18:
    categoria = "Adolescente"
elif idade > 60:
    categoria = "Adulto"
else :
    categoria = "Idoso"

print(" a categoria do cliente é: ", categoria)

if vc >= 500:
    desconto = 20
elif vc <=500:
    desconto = 10
elif vc <=200:
    desconto = 5
else :
    desconto = 0

valordesc = vc * desconto / 100
vf = vc - valordesc

print("---Resumo final da compra---")
print("categoria: ", categoria)
print("Desconto aplicado: ", desconto ,"%")
print("Valor original: ", vc)
print("Valor economizado: R$ ", valordesc)
print("O valor final da compra é: R$ ", vf)

