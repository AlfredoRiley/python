print("Ingesa las coordenadas del punto A: ")
AX=float(input("Ax: "))
AY=float(input("Ay: "))

print("Ingesa las coordenadas del punto B: ")
BX=float(input("Bx: "))
BY=float(input("By: "))

D=((AX-BX)**2+(AY-BY)**2)**0.5

print("------------------------------------")
print("Resultado: ",D)
print("------------------------------------")