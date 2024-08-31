import json

def get_array_list():
    with open("desafio3.json", "r") as faturamentos:
        dados = json.load(faturamentos)
        faturamento_mensal = dados['faturamento_mensal']
        return faturamento_mensal


faturamentos = get_array_list()
faturamento_anual = []

for i in faturamentos:
    faturamento_anual.append(i['faturamento'])

menor_faturamento = min(faturamento_anual)
print(menor_faturamento)
