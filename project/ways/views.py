from django.contrib import messages
from django.shortcuts import render

from .forms import WayForm
from ways.logic import get_ways


def home(request):
    form = WayForm()
    return render(request, 'ways/ways.html', {'form': form})


def find_way(request):
    if request.method == 'POST':
        form = WayForm(request.POST)
        if form.is_valid():
            try:
                context = get_ways(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'ways/ways.html', {'form': form})
            return render(request, 'ways/ways.html', context)
        return render(request, 'ways/ways.html', {'form': form})
    else:
        form = WayForm()
        messages.error(request, 'You did smth wrong')
        return render(request, 'ways/ways.html', {'form': form})
