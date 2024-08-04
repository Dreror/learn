from django.shortcuts import render


def home(request):
    return render(request, "new/home.html")


def about(request):
    return render(request, "new/about.html")


def contact(request):
    return render(request, "new/contact.html")
