from rest_framework import viewsets
from escola.models import Aluno, Curso
from escola.serializer import AlunosSerializer, CursoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exobomdp todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunosSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
