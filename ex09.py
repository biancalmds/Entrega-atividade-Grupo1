import requests

moedas = {
    "USD": "dólares americanos",
    "EUR": "euros",
    "GBP": "libras esterlinas",
    "JPY": "ienes japoneses",
    "ARS": "pesos argentinos",
}

pais_escolhido=input("Digite a sigla da moeda que deseja consultar: ").upper()

key = 'c0bb6ac4cb34bf1fd78986b5'
url = f'https://v6.exchangerate-api.com/v6/{key}/pair/BRL/{pais_escolhido}'
url2 = f'https://v6.exchangerate-api.com/v6/{key}/pair/{pais_escolhido}/BRL'

response = requests.get(url)
data = response.json()
moeda=data['conversion_rate']

response2 = requests.get(url2)
data2 = response2.json()
moeda2=data2['conversion_rate']


print(f'1 {moedas[pais_escolhido]} vale {moeda2} reais')
print(f'1 real vale {moeda} {moedas[pais_escolhido]}')