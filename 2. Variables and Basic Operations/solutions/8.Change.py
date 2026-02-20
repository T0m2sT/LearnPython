change = int(input("What's the change needed? "))
notas_50 = change // 50
change = change % 50
notas_20 = change // 20
change = change % 20
notas_10 = change // 10
change = change % 10
notas_5 = change // 5
change = change % 5
print(notas_50, "50 /", notas_20 , "20 /", notas_10 , "10 /" , notas_5 , "5")

# Extra - In case banknotes are not sufficient, print the remaining change

if change != 0:
    print("Remaining change:", change)