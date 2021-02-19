import requests
from utils.simples_k import curso_url, avaliacoes_url, headers

# result_curso = requests.get(url=f"{curso_url}4/", headers=headers)
# print(result_curso.json()['titulo'])

# result_aval = requests.get(url=f"{avaliacoes_url}4/", headers=headers)
# print(result_aval.json()['nome'])

novo_curso = {
    "titulo": "Criando outro curso via teste API",
    "url": "http://www.minhaurl.com.br/cursos/outro_test_post_api"
}

resultado = requests.post(url=curso_url, headers=headers, data=novo_curso)

assert resultado.status_code == 201

assert resultado.json()['titulo'] == novo_curso['titulo']


