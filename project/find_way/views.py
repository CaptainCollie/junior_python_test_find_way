from django.shortcuts import render


def home(request):
    name = "Jeorge"
    context = {
        "name": name,
    }
    return render(request, "home.html", context=context)
