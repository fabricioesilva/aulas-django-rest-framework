import requests
from utils.simples_k import headers3

curso_url = 'http://localhost:8000/api/v2/cursos/'
avaliacoes_url = 'http://localhost:8000/api/v2/avaliacoes/'


atualiza_curso = {
    "titulo": "Atualiza curso via teste API",
    "url": "http://www.minhaurl.com.br/cursos/test_put_api"
}

resposta = requests.put(url=f'{curso_url}10/',
                        headers=headers3, data=atualiza_curso)

print(resposta.status_code)
print(resposta.json())

assert resposta.status_code == 200

assert resposta.json()["titulo"] == atualiza_curso['titulo']
