from datetime import date

def salario_atual(salario_inicial: float, ano_atual: int = None) -> float:
    if ano_atual is None:
        ano_atual = date.today().year

    ano_base = 1995
    salario = salario_inicial

    if ano_atual <= ano_base:
        return salario

    percentual = 0.015 
    for ano in range(1996, ano_atual + 1):
        salario *= (1 + percentual)
        percentual *= 2

    return salario

try:
    s0_txt = input("Salário inicial em 1995: ").replace(",", ".").strip()
    s0 = float(s0_txt)
    ano_txt = input("Calcular até qual ano? (ENTER = ano atual): ").strip()
    ano = int(ano_txt) if ano_txt else date.today().year

    valor = salario_atual(s0, ano)
    print(f"\nSalário em {ano}: R$ {valor:.2f}")

except ValueError:
    print("Entrada inválida. Tente novamente.")