from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    context = {
        "gif": "this is text"
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')


def packages(request):
    return render(request, 'packages.html')


def webdev(request):
    return render(request, 'webdev.html')


def work(request):
    return render(request, 'work.html')


def basic1(request):
    return render(request, 'packagesingle.html')