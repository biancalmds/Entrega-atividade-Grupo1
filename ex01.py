print("O posto de gasolina está com promoção!\nNa compra de até 20 litros de álcool, desconto de 3% por litro; acima de 20 litros, desconto de 5% por litro.")
print("Já na compra de até 20 litros de gasolina, desconto de 4% por litro; acima de 20 litros, desconto de 6% por litro\nQual deseja comprar?\n")

digito = input('Digite "A" para álcool e "G" para gasolina: ').upper()

if digito == "A":
    qnt_alcool = int(input("Quantos litros de álcool você deseja? "))
    preco_litro = 1.90
    if qnt_alcool > 20:
        valor_pago = qnt_alcool * (preco_litro * 0.95)
    else:
        valor_pago = qnt_alcool * (preco_litro * 0.97)
    print(f"O valor a ser pago será R$ {valor_pago:.2f}")

elif digito == "G":
    qnt_gasolina = int(input("Quantos litros de gasolina você deseja? "))
    preco_litro = 2.50
    if qnt_gasolina > 20:
        valor_pago = qnt_gasolina * (preco_litro * 0.94)
    else:
        valor_pago = qnt_gasolina * (preco_litro * 0.96)
    print(f"O valor a ser pago será R$ {valor_pago:.2f}")