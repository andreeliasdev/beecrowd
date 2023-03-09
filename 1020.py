valor_dias = int(input())

ano = valor_dias//365
resto = valor_dias%365

mes = resto//30
resto = resto%30

dias = resto


print(ano, "ano(s)")
print(mes, "mes(es)")
print(dias, "dia(s)")