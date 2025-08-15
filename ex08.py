import requests

pais = input("Digite o nome em inglês do país que deseja ter acesso aos dados: ")

requisicao = requests.get(f"https://restcountries.com/v3.1/name/{pais}").json()

print(f'''
Nome do país: {list(requisicao[0]["name"]["nativeName"].values())[0]["common"]}
Linguagem: {list(requisicao[0]["languages"].values())[0]}
Região: {requisicao[0].get("region")}
Subregião: {requisicao[0].get("subregion")}
Capital: {requisicao[0].get("capital")[0]}
Sigla da moeda: {list(requisicao[0].get("currencies").keys())[0]}
Nome da moeda: {list(requisicao[0]["currencies"].values())[0]["name"]}
Símbolo da moeda: {list(requisicao[0]["currencies"].values())[0]["symbol"]}
Países que fazem fronteira com o país escolhido: {requisicao[0].get("borders")}
''')