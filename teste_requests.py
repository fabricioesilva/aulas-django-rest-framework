import requests
from utils.simples_k import headers5


# GET avaliações

# avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# print(avaliacoes.status_code) -> 200

# Acessando os dados
# print(avaliacoes.json())
print('------------------------')
# print(avaliacoes.json()['results'][-3]['nome'])

# GET avaliação por id
# avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/4')

# print(avaliacao.json())

# GET cursos


cursos = requests.get(
    url='http://localhost:8000/api/v2/cursos', headers=headers5)

print(cursos.status_code)
print(cursos.json())
