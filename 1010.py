linha1=input().split()
codigo_peca1 = int(linha1[0])
quantidade_peca1 = int(linha1[1])
valor_peca1 = float(linha1[2])

linha2=input().split()
codigo_peca2 = int(linha2[0])
quantidade_peca2 = int(linha2[1])
valor_peca2 = float(linha2[2])

total_peca1 = (quantidade_peca1*valor_peca1)
total_peca2 = (quantidade_peca2*valor_peca2)

valor_a_pagar = (total_peca2+total_peca1)

print("VALOR A PAGAR: R$ %.2f"%valor_a_pagar)