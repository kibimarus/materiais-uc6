def conversor(celsius,fahrenheit):

    fahrenheit = (celsius * 9 / 5) + 32

    print(celsius," ° em Fahrenheit é: ", fahrenheit)


celsius = float (input("Digite a temperatura em Celsius: "))
fahrenheit = float (celsius * 9 / 5) + 32
conversor(celsius, fahrenheit)
