from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def amenities_view(request):
    return render(request, 'amenities.html')

def location_view(request):
    return render(request, 'location.html')

def rooms_view(request):
    return render(request, 'rooms.html')
