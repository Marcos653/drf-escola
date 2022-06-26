from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status

class CursosTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT1', descricao='Curso teste 1', nivel='B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso='CTT2', descricao='Curso teste 2', nivel='A'
        )

    # def test_falhador(self):
    #     self.fail('Teste falhou')

    def test_request_get_list_cursos(self):
        """Teste para verificar a requisicao GET para listar all"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    
    def test_request_post_create(self):
        """Test para verificar a requesicao POST para criar"""
        data = {
            'codigo_curso':"CTT3",
            'descricao':'Curso test 3',
            'nivel':'A'
        }
        response = self.client.post(self.list_url, data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_request_delete(self):
        """Test request DELETE n deve deletar"""
        response = self.client.delete('/cursos/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_request_update(self):
        """Test request UPDATE atualizar curso"""
        data = {
            'codigo_curso':'CTT1',
            'descricao':'Curso teste 1 atualizado',
            'nivel':'I'
        }
        response = self.client.put('/cursos/1/', data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)