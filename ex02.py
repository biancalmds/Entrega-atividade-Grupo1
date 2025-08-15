valor_saque = int(input("Digite o valor do saque (não será possível sacar mais que R$600 e menos que R$10): "))
notas = {
    "nota1": 0,
    "nota5": 0,
    "nota10": 0,
    "nota50": 0,
    "nota100": 0
}

if (valor_saque < 10) or (valor_saque > 600):
    print("Não foi possível realizar o saque!")
else:
    while valor_saque != 0:
        if valor_saque >= 100:
            notas["nota100"] += 1
            valor_saque -= 100
        elif valor_saque >= 50:
            notas["nota50"] += 1
            valor_saque -= 50
        elif valor_saque >= 10:
            notas["nota10"] += 1
            valor_saque -= 10
        elif valor_saque >= 5:
            notas["nota5"] += 1
            valor_saque -= 5
        else:
            notas["nota1"] += 1
            valor_saque -= 1

for nota, quantidade in notas.items():
    if quantidade != 0:
        print(f"{nota}: {quantidade}")