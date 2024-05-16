from django.urls import   path
from . import views


urlpatterns = [
    path("", views.home, name='index'),
    
    #path('accounts/', include('django.contrib.parqueadero.urls')),
    path("usuario",views.lista_usurio, name='usuario'),
    path("loguin",views.loguin, name='login'),
    path("register",views.register, name='register'),
    path("home",views.home, name='home'),
    path("points",views.points, name='points'),
    path("headquarters",views.headquarters, name='headquarters'),
    path("my_account",views.my_account, name='my_account'),
    path("cerrar-sesion",views.cerrar_sesion, name='cerrar-sesion'),
    path("estacion-centro",views.season_cen, name='estacion_centro'),
    path("estacion-damian",views.season_dam, name='estacion_damian'),
    path("estacion-centro/a",views.cen_estacion_a, name='estacion_centro_puntos'),
    path("estacion-centro/<slug:slug>",views.cen_estacion_otros, name='estacion_centro_puntos'),
    path("estacion-dam/<slug:slug>",views.dam_estacion_otros, name='estacion_damian_puntos'),
    path("punto/<int:id>",views.punto, name='punto'),
    path("validar/<int:id>/<str:password>", views.validar_punto, name='validar'),
    path("liberar/<int:id>", views.liberar, name="liberar")
    
]