import requests
from utils.simples_k import headers4


class TesteCursos:
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_base_cursos, headers=self.headers4)

        assert cursos.status_code == 200

    def test_get_curso(self):
        curso = requests.get(
            url=f'{self.url_base_cursos}4/', headers=self.headers4)

        assert curso.status_code == 200

    def test_post_curso(self):
        novo = {
            'titulo': 'Curso de Programação em Ruby 3',
            'url': 'http://www.cursoruby.com.br/ruby3'
        }

        resposta = requests.post(
            url=self.url_base_cursos, headers=self.headers4, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            'titulo': 'Atualiza curso via teste API 2',
            'url': 'http://www.minhaurl.com.br/cursos/test_put_api'
        }

        resposta = requests.put(
            url=f'{self.url_base_cursos}10/', headers=self.headers4, data=atualizado)

        assert resposta.status_code == 200
        # assert resposta.json()['titulo'] == atualizado['titulo']

    def test_put_titulo_curso(self):
        atualizado = {
            'titulo': 'Atualiza curso via teste API 3',
            'url': 'http://www.minhaurl.com.br/cursos/test_put_api2'
        }

        resposta = requests.put(
            url=f'{self.url_base_cursos}10/', headers=self.headers4, data=atualizado)


''
        assert resposta.status_code == 200

    def test_delete_curso(self):
        resposta = requests.delete(
            url=f'{self.url_base_cursos}12/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0
