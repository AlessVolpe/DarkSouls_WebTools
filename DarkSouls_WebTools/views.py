from django.shortcuts import render

def landing_page(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
