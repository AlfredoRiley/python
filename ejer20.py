print("ingrese los valoderes de x1,y1,z1:")
x1=float(input("X1: "))
y1=float(input("Y1: "))
z1=float(input("Z1: "))

print("ingrese los valoderes de x2,y2,z2:")
x2=float(input("X2: "))
y2=float(input("Y2: "))
z2=float(input("Z2: "))

dis=((z2-z1)**2+(y2-y1)**2+(x2-x1)**2)**0.5

print("La distancia es:",dis)