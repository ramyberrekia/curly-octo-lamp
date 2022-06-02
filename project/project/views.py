from django.shortcuts import render

def Handler_404(request):
    return render(request, '404.html', status=404)