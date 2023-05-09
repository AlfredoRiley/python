c= -1
I= 0
m= 0
while (c<0) or (I>=0) or (I>=100) or (m<=0):
    print("ingrese los datos")

    c=int(input("capital: "))
    I=int(input("interes: "))
    m=int(input("tiempo en años: "))
for i in range(m):
    c = c*(1+I/100)

print("Tienes",c,"soles")