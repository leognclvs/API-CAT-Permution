from rest_framework import serializers
from .models import *

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'

class OrdemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordem
        fields = '__all__'

class StartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Start
        fields = '__all__'

class ServicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicos
        fields = '__all__'

class PressurizadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pressurizador
        fields = '__all__'

class FiltrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filtros
        fields = '__all__'

class DosagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dosagem
        fields = '__all__'

class DesmiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desmi
        fields = '__all__'

class OsmoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Osmose
        fields = '__all__'

class LeitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leito
        fields = '__all__'

class AfericaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Afericao
        fields = '__all__'

class OzonioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ozonio
        fields = '__all__'

class UvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uv
        fields = '__all__'

class RecupRejeitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recup_Rejeito
        fields = '__all__'

class AnaliseAguaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analise_Agua
        fields = '__all__'

class TreinamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treinamento
        fields = '__all__'

class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parte_Tec
        fields = '__all__'

class ConferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conferencia
        fields = '__all__'