from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

class TreinamentoView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = TreinamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def Cat_Conf(request):
    # Recuperar todos os números de CAT que estão na tabela Info
    all_cats_conf = Info.objects.values_list('cat_number', flat=True)

    # Recuperar todos os números de CAT que já foram usados na tabela Ordem
    used_cats_conf = Conferencia.objects.values_list('cat_number', flat=True)

    # Filtrar os números de CAT disponíveis
    available_cats_conf = Info.objects.exclude(cat_number__in=used_cats_conf).values_list('cat_number', flat=True)

    return Response(available_cats_conf)
        
@api_view(['GET'])
def Cat_Ordem(request):
    # Recuperar todos os números de CAT que estão na tabela Info
    all_cats_ordem = Info.objects.values_list('cat_number', flat=True)

    # Recuperar todos os números de CAT que já foram usados na tabela Ordem
    used_cats_ordem = Ordem.objects.values_list('cat_number', flat=True)

    # Filtrar os números de CAT disponíveis
    available_cats_ordem = Info.objects.exclude(cat_number__in=used_cats_ordem).values_list('cat_number', flat=True)

    return Response(available_cats_ordem)

@api_view(['GET'])
def Cat_Start(request):
    # Recuperar todos os números de CAT que estão na tabela Info
    all_cats_start = Info.objects.values_list('cat_number', flat=True)

    # Recuperar todos os números de CAT que já foram usados na tabela Start
    used_cats_start = Start.objects.values_list('cat_number', flat=True)

    # Filtrar os números de CAT disponíveis
    available_cats_start = Info.objects.exclude(cat_number__in=used_cats_start).values_list('cat_number', flat=True)

    return Response(available_cats_start)

@api_view(['GET'])
def Cat_Servicos(request):
    # Recuperar todos os números de CAT que estão na tabela Info
    all_cats_serv = Info.objects.values_list('cat_number', flat=True)

    # Recuperar todos os números de CAT que já foram usados na tabela Start
    used_cats_serv = Servicos.objects.values_list('cat_number', flat=True)

    # Filtrar os números de CAT disponíveis
    available_cats_serv = Info.objects.exclude(cat_number__in=used_cats_serv).values_list('cat_number', flat=True)

    return Response(available_cats_serv)

@api_view(['GET'])
def Cat_Press(request):
    # Recuperar todos os números de CAT que estão na tabela Info
    all_cats_press = Info.objects.values_list('cat_number', flat=True)

    # Recuperar todos os números de CAT que já foram usados na tabela Start
    used_cats_press = Pressurizador.objects.values_list('cat_number', flat=True)

    # Filtrar os números de CAT disponíveis
    available_cats_press = Info.objects.exclude(cat_number__in=used_cats_press).values_list('cat_number', flat=True)

    return Response(available_cats_press)

@api_view(['GET'])
def Cat_Filtros(request):
    # Recuperar todos os números de CAT que estão na tabela Info
    all_cats_filtros = Info.objects.values_list('cat_number', flat=True)

    # Recuperar todos os números de CAT que já foram usados na tabela Start
    used_cats_filtros = Filtros.objects.values_list('cat_number', flat=True)

    # Filtrar os números de CAT disponíveis
    available_cats_filtros = Info.objects.exclude(cat_number__in=used_cats_filtros).values_list('cat_number', flat=True)

    return Response(available_cats_filtros)

@api_view(['GET'])
def Cat_Dosagem(request):
    # Recuperar todos os números de CAT que estão na tabela Info
    all_cats_dos = Info.objects.values_list('cat_number', flat=True)

    # Recuperar todos os números de CAT que já foram usados na tabela Start
    used_cats_dos = Dosagem.objects.values_list('cat_number', flat=True)

    # Filtrar os números de CAT disponíveis
    available_cats_dos = Info.objects.exclude(cat_number__in=used_cats_dos).values_list('cat_number', flat=True)

    return Response(available_cats_dos)

@api_view(['GET'])
def Cat_Desmi(request):
    # Recuperar todos os números de CAT que estão na tabela Info
    all_cats_desmi = Info.objects.values_list('cat_number', flat=True)

    # Recuperar todos os números de CAT que já foram usados na tabela Start
    used_cats_desmi = Desmi.objects.values_list('cat_number', flat=True)

    # Filtrar os números de CAT disponíveis
    available_cats_desmi = Info.objects.exclude(cat_number__in=used_cats_desmi).values_list('cat_number', flat=True)

    return Response(available_cats_desmi)

@api_view(['GET'])
def Cat_Osmose(request):
    # Recuperar todos os números de CAT que estão na tabela Info
    all_cats_osm = Info.objects.values_list('cat_number', flat=True)

    # Recuperar todos os números de CAT que já foram usados na tabela Start
    used_cats_osm = Osmose.objects.values_list('cat_number', flat=True)

    # Filtrar os números de CAT disponíveis
    available_cats_osm = Info.objects.exclude(cat_number__in=used_cats_osm).values_list('cat_number', flat=True)

    return Response(available_cats_osm)

@api_view(['GET'])
def Cat_Leito(request):
    # Recuperar todos os números de CAT que estão na tabela Info
    all_cats_lei = Info.objects.values_list('cat_number', flat=True)

    # Recuperar todos os números de CAT que já foram usados na tabela Start
    used_cats_lei = Leito.objects.values_list('cat_number', flat=True)

    # Filtrar os números de CAT disponíveis
    available_cats_lei = Info.objects.exclude(cat_number__in=used_cats_lei).values_list('cat_number', flat=True)

    return Response(available_cats_lei)

@api_view(['GET'])
def Cat_Afericao(request):
    # Recuperar todos os números de CAT que estão na tabela Info
    all_cats_afe = Info.objects.values_list('cat_number', flat=True)

    # Recuperar todos os números de CAT que já foram usados na tabela Start
    used_cats_afe = Afericao.objects.values_list('cat_number', flat=True)

    # Filtrar os números de CAT disponíveis
    available_cats_afe = Info.objects.exclude(cat_number__in=used_cats_afe).values_list('cat_number', flat=True)

    return Response(available_cats_afe)

@api_view(['GET'])
def Cat_Ozonio(request):
    # Recuperar todos os números de CAT que estão na tabela Info
    all_cats_ozonio = Info.objects.values_list('cat_number', flat=True)

    # Recuperar todos os números de CAT que já foram usados na tabela Start
    used_cats_ozonio = Ozonio.objects.values_list('cat_number', flat=True)

    # Filtrar os números de CAT disponíveis
    available_cats_ozonio = Info.objects.exclude(cat_number__in=used_cats_ozonio).values_list('cat_number', flat=True)

    return Response(available_cats_ozonio)

@api_view(['GET'])
def Cat_Uv(request):
    # Recuperar todos os números de CAT que estão na tabela Info
    all_cats_uv = Info.objects.values_list('cat_number', flat=True)

    # Recuperar todos os números de CAT que já foram usados na tabela Start
    used_cats_uv = Uv.objects.values_list('cat_number', flat=True)

    # Filtrar os números de CAT disponíveis
    available_cats_uv = Info.objects.exclude(cat_number__in=used_cats_uv).values_list('cat_number', flat=True)

    return Response(available_cats_uv)

@api_view(['GET'])
def Cat_Rejeito(request):
    # Recuperar todos os números de CAT que estão na tabela Info
    all_cats_rej = Info.objects.values_list('cat_number', flat=True)

    # Recuperar todos os números de CAT que já foram usados na tabela Start
    used_cats_rej = Recup_Rejeito.objects.values_list('cat_number', flat=True)

    # Filtrar os números de CAT disponíveis
    available_cats_rej = Info.objects.exclude(cat_number__in=used_cats_rej).values_list('cat_number', flat=True)

    return Response(available_cats_rej)

@api_view(['GET'])
def Cat_Agua(request):
    # Recuperar todos os números de CAT que estão na tabela Info
    all_cats_agua = Info.objects.values_list('cat_number', flat=True)

    # Recuperar todos os números de CAT que já foram usados na tabela Start
    used_cats_agua = Analise_Agua.objects.values_list('cat_number', flat=True)

    # Filtrar os números de CAT disponíveis
    available_cats_agua = Info.objects.exclude(cat_number__in=used_cats_agua).values_list('cat_number', flat=True)

    return Response(available_cats_agua)

@api_view(['GET'])
def Cat_Tec(request):
    # Recuperar todos os números de CAT que estão na tabela Info
    all_cats_tec = Info.objects.values_list('cat_number', flat=True)

    # Recuperar todos os números de CAT que já foram usados na tabela Start
    used_cats_tec = Parte_Tec.objects.values_list('cat_number', flat=True)

    # Filtrar os números de CAT disponíveis
    available_cats_tec = Info.objects.exclude(cat_number__in=used_cats_tec).values_list('cat_number', flat=True)

    return Response(available_cats_tec)

class InfoViewSet(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

class OrdemViewSet(viewsets.ModelViewSet):
    queryset = Ordem.objects.all()
    serializer_class = OrdemSerializer

class StartViewSet(viewsets.ModelViewSet):
    queryset = Start.objects.all()
    serializer_class = StartSerializer

class ServicosViewSet(viewsets.ModelViewSet):
    queryset = Servicos.objects.all()
    serializer_class = ServicosSerializer

class PressurizadorViewSet(viewsets.ModelViewSet):
    queryset = Pressurizador.objects.all()
    serializer_class = PressurizadorSerializer

class FiltrosViewSet(viewsets.ModelViewSet):
    queryset = Filtros.objects.all()
    serializer_class = FiltrosSerializer

class DosagemViewSet(viewsets.ModelViewSet):
    queryset = Dosagem.objects.all()
    serializer_class = DosagemSerializer

class DesmiViewSet(viewsets.ModelViewSet):
    queryset = Desmi.objects.all()
    serializer_class = DesmiSerializer

class OsmoseViewSet(viewsets.ModelViewSet):
    queryset = Osmose.objects.all()
    serializer_class = OsmoseSerializer

class LeitoViewSet(viewsets.ModelViewSet):
    queryset = Leito.objects.all()
    serializer_class = LeitoSerializer

class AfericaoViewSet(viewsets.ModelViewSet):
    queryset = Afericao.objects.all()
    serializer_class = AfericaoSerializer

class OzonioViewSet(viewsets.ModelViewSet):
    queryset = Ozonio.objects.all()
    serializer_class = OzonioSerializer

class UvViewSet(viewsets.ModelViewSet):
    queryset = Uv.objects.all()
    serializer_class = UvSerializer

class RecupRejeitoViewSet(viewsets.ModelViewSet):
    queryset = Recup_Rejeito.objects.all()
    serializer_class = RecupRejeitoSerializer

class AnaliseAguaViewSet(viewsets.ModelViewSet):
    queryset = Analise_Agua.objects.all()
    serializer_class = AnaliseAguaSerializer

class TreinamentoViewSet(viewsets.ModelViewSet):
    queryset = Treinamento.objects.all()
    serializer_class = TreinamentoSerializer

class TecnicosViewSet(viewsets.ModelViewSet):
    queryset = Parte_Tec.objects.all()
    serializer_class = TecnicoSerializer

class ConferenciaViewSet(viewsets.ModelViewSet):
    queryset = Conferencia.objects.all()
    serializer_class = ConferenciaSerializer