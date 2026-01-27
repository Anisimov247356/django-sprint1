from django.shortcuts import render


def about(request):
    """
    Отображает страницу о сайте.
    Использует шаблон 'pages/about.html'
    """
    return render(request, 'pages/about.html')


def rules(request):
    """
    Отображает страницу с равилами.
    использует шаблон 'pages/rules.html'
    """
    return render(request, 'pages/rules.html')
