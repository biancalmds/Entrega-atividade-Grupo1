salario_inicial = float(input("Digite o salário inicial: "))
ano_inicial = 1995
ano_final = 2025
salario_atual = salario_inicial

percentual = 0.015
salario_atual *= (1 + percentual)

for ano in range(1997, ano_final + 1):
    percentual *= 2
    salario_atual *= (1 + percentual)

print(f"Salário em {ano_final}: R$ {salario_atual:.2f}")
