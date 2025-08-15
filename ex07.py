lista_num = []

while True:
    num = int(input("Digite um número ou -1 para parar: "))
    if num == -1:
        break
    else:
        lista_num.append(num)


valores_acima_media = [numero for numero in lista_num if numero > (sum(lista_num)/len(lista_num))]        

print(f'''
Quantidade de valores lidos: {len(lista_num)}
Valores na ordem em que foram informados: {lista_num}
Valores na ordem inversa à que foram informados: {lista_num[::-1]}
Soma dos valores: {sum(lista_num)}
Média dos valores: {sum(lista_num)/len(lista_num)}
Quantidade de valores acima da média: {len(valores_acima_media)}
''')