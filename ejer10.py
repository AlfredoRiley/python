PI=3.1416

print("Ingrsa los datos del silindor:")
RAD=int(input("radio: "))
ALT=int(input("altura: "))

VOL=PI*RAD**2*ALT
ARE=2*PI*RAD*(ALT+RAD)

print("--------------------------")
print("Volumen:",VOL)
print("--------------------------")
print("Area:",ARE)
print("--------------------------")