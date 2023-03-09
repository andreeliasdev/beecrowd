segundos = int(input())

hora = segundos//3600
resto = segundos%3600

minutos = resto//60
resto = resto%60

segundo = resto

print(hora,minutos,segundo, sep=":")