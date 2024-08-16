from django.urls import path, include
from rest_framework.routers import DefaultRouter
from catback.views import *
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'info', InfoViewSet)
router.register(r'ordem', OrdemViewSet)
router.register(r'start', StartViewSet)
router.register(r'servicos', ServicosViewSet)
router.register(r'pressurizador', PressurizadorViewSet)
router.register(r'filtros', FiltrosViewSet)
router.register(r'dosagem', DosagemViewSet)
router.register(r'desmi', DesmiViewSet)
router.register(r'osmose', OsmoseViewSet)
router.register(r'leito', LeitoViewSet)
router.register(r'afericao', AfericaoViewSet)
router.register(r'ozonio', OzonioViewSet)
router.register(r'uv', UvViewSet)
router.register(r'recup_rejeito', RecupRejeitoViewSet)
router.register(r'analise_agua', AnaliseAguaViewSet)
router.register(r'treinamento', TreinamentoViewSet)
router.register(r'tecnicos', TecnicosViewSet)

urlpatterns = [
    path('', include(router.urls)),
     path('cats-ordem/', Cat_Ordem),
    path('catstart/', Cat_Start),
    path('catservicos/', Cat_Servicos),
    path('catpress/', Cat_Press),
    path('catfiltros/', Cat_Filtros),
    path('catdosagem/', Cat_Dosagem),
    path('catdesmi/', Cat_Desmi),
    path('catosmose/', Cat_Osmose),
    path('catleito/', Cat_Leito),
    path('catafericao/', Cat_Afericao),
    path('catozonio/', Cat_Ozonio),
    path('catuv/', Cat_Uv),
    path('catrejeito/', Cat_Rejeito),
    path('catagua/', Cat_Agua),
    path('cattec/', Cat_Tec),
    path('catconf/', Cat_Conf),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
