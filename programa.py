# programa para comvertir una cantidad dada en grados centigrados en su equivalente en grados fharenheit

print("--------------------------------")
print("----Conversor de Temperatura----")
print("--------------------------------")

# input
C = int(input (" digite el valor de C: "))

#processing
F = (C * 1.8 + 32)
K = ( C + 273.15)

#ouput
print("---------------------------------")
print("------------RESULTADOS-----------")
print("---------------------------------")
print("la convercion de " + str(C) + " grados celcius a grados fharenheint es " + str(F))
print("la convercion de " + str(C) + " grados celcius a grados Kelvin es " + str(K))
