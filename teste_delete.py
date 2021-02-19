import requests
from utils.simples_k import headers2


resultado = requests.delete(url=f'{curso_url}11/', headers=headers2)

assert resultado.status_code == 204

assert len(resultado.text) == 0
