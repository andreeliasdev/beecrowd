linha1 = input().split()
A = int(linha1[0])
B = int(linha1[1])
C = int(linha1[2])

maiorAB = int(((A+B+abs(A-B))/2))
maiorAC = int(((A+C+abs(A-C))/2))

if (maiorAC>maiorAB):
    print(maiorAC,"eh o maior")
else:
    print(maiorAB,"eh o maior")