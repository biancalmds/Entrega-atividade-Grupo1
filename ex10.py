import requests

cep = input("Digite o CEP do endereço de destino sem pontuações: ")
cep = cep.replace("-", "")
requisicao = requests.get(f"https://viacep.com.br/ws/{cep}/json").json()

if "01000" < cep < "01599":
    zona_sp = "Centro de São Paulo"
elif "02000" < cep < "02999":
    zona_sp = "Zona Norte de São Paulo"
elif ("03000" < cep < "03999") or ("08000" < cep < "08499"):
    zona_sp = "Zona Leste de São Paulo"
elif "04000" < cep < "04999":
    zona_sp = "Zona Sul de São Paulo"
elif "05000" < cep < "05899":
    zona_sp = "Zona Oeste de São Paulo"
else:
    zona_sp = "Fora da Grande São Paulo"

print(f"Bairro: {requisicao.get("bairro")}, {zona_sp}")