import requests
import jsonpath


# Avaliacoes

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes')

resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')
# print(resultados[0])
# uso do jsonpath permite  ex: 'results[0].nome'

primeiros = jsonpath.jsonpath(avaliacoes.json(), 'results[0].avaliacao')
print(primeiros[0])

nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')

notas = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')

print(nomes)
print(notas)
