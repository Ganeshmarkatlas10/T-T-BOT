from django.shortcuts import render

def load_home_page(request):
    return render(request, "homepage.html")


def load_features(request):
    return render(request, "features.html")


def load_contact_us(request):
    return render(request, "contact us.html")

def load_about_us(request):
    return render(request, "aboutus.html")