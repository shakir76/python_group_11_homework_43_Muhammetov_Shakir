from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html")


def one_post(request):
    return render(request, "one.html")


def two_post(request):
    return render(request, "two.html")


def three_post(request):
    return render(request, "thee.html")
