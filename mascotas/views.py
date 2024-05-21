from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mis_mascotas(request):
        return HttpResponse("""
                <h1>Mis Mascotas</h1>
                <p>Zoe, Ayun y Negrito</p>
                <img src="" alt="Zoe">
                <img src="" alt="Ayun">
                <img src="" alt="Negrito">
        """)