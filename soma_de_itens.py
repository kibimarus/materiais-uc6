produtos = [6, 12, 18, 28, 64, 72, 114, 240]
 
total = 0

 
for s in produtos:
    print("Atual", total)
    print (total, " + ", s, "=" )
    total=total+s
    print(total)
    print("_"*10)
 
 
 
print ("O total somado é: ", total)