from django.shortcuts import render

def home(request):
    """Home page view"""
    context = {
        'title': 'Welcome to My Personal Website',
        'name': 'Jai Ohri',
        'tagline': 'Developer, Designer, and Problem Solver',
        'about': 'I am passionate about creating innovative solutions and building meaningful digital experiences.',
    }
    return render(request, 'pages/home.html', context)
