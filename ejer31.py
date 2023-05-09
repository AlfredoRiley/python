print("Ingrese la fecha")
A=int(input("Año: "))
M=int(input("Mes: "))
D=int(input("Día: "))

if D>0 and D<30:
    print("Mañana es",D+1,"del mes",M,"del Año",A)
else:
    if M>0 and M<12:
        print("Mañana es",D,"del mes",M+1,"del Año",A)
    else:
        print("Mañana es",D,"del mes",M,"del Año",A+1)
