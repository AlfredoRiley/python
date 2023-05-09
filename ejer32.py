print("Ingrese las velocidades de ambos vehiculos")
v1=float(input("Velocidad 1:"))
v2=float(input("Velocidad 2:"))

print("¿A que distancia se encuentran?")
d=float(input("Distancia en metros: "))

if v1>0 and v2>0:
    t=d/(v1+v2)
    print("impactan en",t)
else:
    print("!!!!ESTAS MAAAAAL TIRE ERROR!!!!!")
