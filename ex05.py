cardapio = {
    100: ("Cachorro Quente", 1.20),
    101: ("Bauru Simples", 1.30),
    102: ("Bauru com Ovo", 1.50),
    103: ("Hambúrguer", 1.20),
    104: ("Cheeseburguer", 1.30),
    105: ("Refrigerante", 1.00)
}

pedido = {
    100: 0,
    101: 0,
    102: 0,
    103: 0,
    104: 0,
    105: 0
}

while True:
    codigo = int(input("Digite o código do item desejado: "))
    quantidade = int(input(f"Digite a quantidade de {cardapio[codigo][0]} desejada: "))
    pedido[codigo] += (cardapio[codigo][1] * quantidade)
    continuar = input("Deseja continuar comprando? (S/N): ").upper()
    if continuar == "N":
        break

print("\nVALOR A SER PAGO POR ITEM: ")
for codigo, preco in pedido.items():
    if preco != 0:
       print(f"- {cardapio[codigo][0]}: R${preco:.2f}")

print(f"\nTOTAL GERAL DO PEDIDO: R${sum(list(pedido.values())):.2f}")
