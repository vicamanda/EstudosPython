temp = float(input("Insira a temperatura: "))

if temp < 37:
    print("normal")
elif temp >= 37 and temp < 38:
    print("febril")
else:
    print("febre alta")