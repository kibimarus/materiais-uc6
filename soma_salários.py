salarios =  [20000, 3000, 3200, 1700, 12000, 2500]

total = 0

#? Somaremos todos os salários 
for sala in salarios:
        print("Atual: ", total)
        print(total, " + ", sala, " = " )
        total = total + sala
        print(total)
        print("_"*25)

print("O total somado é: ", total)
