def calculando_imc(peso,altura):
    calculo = peso/altura ** 2

    if calculo < 18.5:
        print("Abaixo do peso")
 
    elif calculo >= 18.5:
        print("Peso normal") 

    elif calculo <= 25 and calculo >= 29.99:
        print("Sobrepeso")

    else:
        print("Obesidade")


print("-----CALCULADORA DE IMC-----")
peso = (float(input("Para começar digite seu peso: ")))
altura = (float(input("Agora digite sua altura: ")))
calculando_imc(peso,altura)
