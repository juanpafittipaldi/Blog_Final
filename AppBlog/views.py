from django.shortcuts import render
def lista_posteos(request):
    return render(request, 'html/lista_posteos.html', {})
