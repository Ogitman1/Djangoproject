from django.shortcuts import render
from django.http import HttpResponse
from .models import Dados
# Create your views here.
def mainpage(request):
   dados = Dados.objects.all()
   return render(request, 'mainpage.html', {'dados': dados})