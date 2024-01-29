from django.urls import path
from .views import home, iniciar_audio, parar_audio

urlpatterns = [
    path('', home, name='home'),
    path('iniciar_audio/<str:texto>/<int:numero_de_vezes>/', iniciar_audio, name='iniciar_audio'),
    path('parar_audio/', parar_audio, name='parar_audio'),
]
