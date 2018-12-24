from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, render_to_response


def index(request):
    return render(request,"index.html")
def contact(request):
    return render(request,"contact.html")
def currenttimings(request):
    return render(request,"currenttimings.html")
def liverunningstatus(request):
    return render(request,"liverunningstatus.html")
#def pnrstatus(request):
  #  return render(request,"pnrstatus.html")
def trainno(request):
    return render(request,"trainno.html")
def traintimings(request):
    return render(request,"traintimings.html")