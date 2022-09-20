print("INgrese año")
año=int(input("año: "))

if (año % 400==0)or(año % 4==0)and(año % 100!=0):
    print("El año es BISIESTO")
else:
    print("El año NO es BISIESTO")