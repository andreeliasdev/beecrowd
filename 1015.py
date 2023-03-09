linha1 = input().split()
X1 = float(linha1[0])
Y1 = float(linha1[1])

linha2 = input().split()
X2 = float(linha2[0])
Y2 = float(linha2[1])

distancia = (((X2-X1)**2)+((Y2-Y1)**2))**(1/2)

print("{:.4f}".format(distancia))