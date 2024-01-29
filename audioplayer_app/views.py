from django.shortcuts import render

from django.http import JsonResponse
import pyttsx3
from threading import Thread
import pygame

pygame.mixer.init()

is_playing = False

def gerar_audio(texto, numero_de_vezes):
    global is_playing
    is_playing = True

    for _ in range(numero_de_vezes):
        if not is_playing:
            break 

        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(texto)
        engine.runAndWait()
       

def home(request):
    return render(request, 'home.html')

def iniciar_audio(request, texto, numero_de_vezes):
    global is_playing
    
    if not is_playing:
        is_playing = True
        audio_thread = Thread(target=gerar_audio, args=(texto, int(numero_de_vezes)))
        audio_thread.start()
        response_data = {'status': 'success', 'message': 'Áudio em reprodução'}
    else:
        response_data = {'status': 'error', 'message': 'Já há uma reprodução em andamento'}

    return JsonResponse(response_data)

def parar_audio(request):
    global is_playing
    is_playing = False
    pygame.mixer.music.stop()
    response_data = {'status': 'success', 'message': 'Geração de áudio parada'}
    return JsonResponse(response_data)


# Create your views here.
