menu = {
    100: ("Cachorro Quente", 1.20),
    101: ("Bauru Simples", 1.30),
    102: ("Bauru com Ovo", 1.50),
    103: ("Hambúrguer", 1.20),
    104: ("Cheeseburguer", 1.30),
    105: ("Refrigerante", 1.00),
}

print("Lanchonete")
print("Digite o código do item e a quantidade.")
print("Aperte e 'ENTER' para encerrar o pedido.\n")

pedido = [] 

while True:
    cod_txt = input("Código do item (ENTER para encerrar): ").strip()
    if cod_txt == "":
        break
    if not cod_txt.isdigit() or int(cod_txt) not in menu:
        print(">> Código inválido. Tente de novo.\n")
        continue

    cod = int(cod_txt)
    nome, preco = menu[cod]

    try:
        qtd = int(input(f"Quantidade de '{nome}': ").strip())
        if qtd <= 0:
            print(">> Quantidade deve ser positiva.\n")
            continue
    except ValueError:
        print(">> Quantidade inválida.\n")
        continue

    subtotal = preco * qtd
    pedido.append((nome, preco, qtd, subtotal))
    print(f"Adicionado: {nome} x{qtd}  -> R$ {subtotal:.2f}\n")

print("\n CUPOM FISCAL")
total = 0.0
for nome, preco, qtd, subtotal in pedido:
    total += subtotal
    print(f"{nome:16} {qtd:>3} x R$ {preco:>4.2f} = R$ {subtotal:>6.2f}")
print("-" * 38)
print(f"TOTAL: R$ {total:>6.2f}")