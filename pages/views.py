from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages

def home(request):
    """Home page view"""
    context = {
        'title': 'Welcome to My Personal Website',
        'name': 'Jai Ohri',
        'tagline': 'Developer, Designer, and Problem Solver',
        'about': 'I am passionate about creating innovative solutions and building meaningful digital experiences.',
    }
    return render(request, 'pages/home.html', context)

def about(request):
    """About page view"""
    context = {
        'title': 'About Me',
        'name': 'Jai Ohri',
        'tagline': 'Developer, Designer, and Problem Solver',
        'about': 'I am passionate about creating innovative solutions and building meaningful digital experiences.',
        'skills': [
            {'name': 'Python', 'icon': '🐍', 'level': 90},
            {'name': 'Django', 'icon': '🎯', 'level': 85},
            {'name': 'React', 'icon': '⚛️', 'level': 80},
            {'name': 'JavaScript', 'icon': '💎', 'level': 85},
            {'name': 'HTML/CSS', 'icon': '🎨', 'level': 90},
            {'name': 'PostgreSQL', 'icon': '🐘', 'level': 75},
        ],
        'experience': [
            {
                'title': 'Full Stack Developer',
                'company': 'Tech Company',
                'period': '2022 - Present',
                'description': 'Developing web applications using Django, React, and modern web technologies.'
            },
            {
                'title': 'Frontend Developer',
                'company': 'Startup Inc',
                'period': '2020 - 2022',
                'description': 'Created responsive user interfaces and improved user experience across multiple platforms.'
            }
        ]
    }
    
    # Check if request is HTMX
    if request.headers.get('HX-Request'):
        return render(request, 'pages/about_content.html', context)
    
    return render(request, 'pages/about.html', context)

def portfolio(request):
    """Portfolio page view"""
    context = {
        'title': 'My Portfolio',
        'name': 'Jai Ohri',
        'projects': [
            {
                'title': 'E-commerce Platform',
                'description': 'A full-stack e-commerce solution built with Django and React',
                'technologies': ['Django', 'React', 'PostgreSQL', 'Stripe'],
                'image': 'https://via.placeholder.com/400x300/4F46E5/FFFFFF?text=E-commerce+Platform',
                'github_url': '#',
                'live_url': '#'
            },
            {
                'title': 'Task Management App',
                'description': 'A collaborative task management application with real-time updates',
                'technologies': ['Django', 'WebSockets', 'JavaScript', 'Bootstrap'],
                'image': 'https://via.placeholder.com/400x300/10B981/FFFFFF?text=Task+Management',
                'github_url': '#',
                'live_url': '#'
            },
            {
                'title': 'Weather Dashboard',
                'description': 'A responsive weather dashboard with location-based forecasts',
                'technologies': ['React', 'API Integration', 'Chart.js', 'CSS3'],
                'image': 'https://via.placeholder.com/400x300/F59E0B/FFFFFF?text=Weather+Dashboard',
                'github_url': '#',
                'live_url': '#'
            },
            {
                'title': 'Blog Platform',
                'description': 'A content management system with rich text editing capabilities',
                'technologies': ['Django', 'Django REST Framework', 'Vue.js', 'PostgreSQL'],
                'image': 'https://via.placeholder.com/400x300/EF4444/FFFFFF?text=Blog+Platform',
                'github_url': '#',
                'live_url': '#'
            }
        ]
    }
    
    # Check if request is HTMX
    if request.headers.get('HX-Request'):
        return render(request, 'pages/portfolio_content.html', context)
    
    return render(request, 'pages/portfolio.html', context)

def contact(request):
    """Contact page view"""
    context = {
        'title': 'Get In Touch',
        'name': 'Jai Ohri',
        'contact_info': {
            'email': 'jai@example.com',
            'phone': '+1 (555) 123-4567',
            'location': 'San Francisco, CA',
            'linkedin': 'https://linkedin.com/in/jai-ohri',
            'github': 'https://github.com/jai-ohri',
            'twitter': 'https://twitter.com/jai_ohri'
        }
    }
    
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Here you would typically save to database or send email
        # For now, we'll just return a success message
        
        if request.headers.get('HX-Request'):
            return render(request, 'pages/contact_success.html', {
                'message': f'Thank you {name}! Your message has been sent successfully.'
            })
        else:
            messages.success(request, f'Thank you {name}! Your message has been sent successfully.')
    
    # Check if request is HTMX
    if request.headers.get('HX-Request'):
        return render(request, 'pages/contact_content.html', context)
    
    return render(request, 'pages/contact.html', context)
