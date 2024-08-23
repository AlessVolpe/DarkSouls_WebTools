from django.shortcuts import render

def landing_page(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')

def error_404(request, exception):
    return render(request, 'error_templates/404.html', status=404)

def error_500(request):
    return render(request, 'error_templates/500.html', status=500)


