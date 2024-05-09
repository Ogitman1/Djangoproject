from django.shortcuts import render
from django.http import HttpResponse
from .models import Dados
# Create your views here.
def mainpage(request):
   dados = Dados.objects.all()
   notas = [2, 5,6, 7, 8, 10]
   return render(request, 'mainpage.html', {'dados': dados, 'notas': notas})