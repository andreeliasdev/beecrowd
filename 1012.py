linha1 = input().split()
A = float(linha1[0])
B = float(linha1[1])
C = float(linha1[2])

area_triangulo = ((A * C)/2)

pi = 3.14159
area_circulo = (pi * (C**2))

area_trapezio = (((A+B)*C)/2)

area_quadrado = (B**2)

area_retangulo = (A*B)

print("TRIANGULO: %.3f"%area_triangulo)
print("CIRCULO: %.3f"%area_circulo)
print("TRAPEZIO: %.3f"%area_trapezio)
print("QUADRADO: %.3f"%area_quadrado)
print("RETANGULO: %.3f"%area_retangulo)