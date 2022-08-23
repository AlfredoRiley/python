import math

print("ingrese GB: ")
GB = float(input())

MG=GB*1024
MD=MG/1.44

print("SALIDA: ")
print("---------------------------------")
print(MD)

print("Numero de discos necesarios: ", math.ceil(MD))