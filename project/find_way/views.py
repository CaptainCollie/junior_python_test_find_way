from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from find_way.models import City
from .forms import CityForm

__all__ = (
    'cities',
    'CityDetailView',
    'CityCreateView',
    'CityUpdateView',
    'CityDeleteView',
    'CityListView',
)


def home(request):
    return render(request, "home.html")


def cities(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    form = CityForm()
    qs = City.objects.all()
    lst = Paginator(qs, 100)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "form": form,
    }
    return render(request, "cities.html", context=context)


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = "detail.html"


class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = "create.html"
    success_url = reverse_lazy('cities')


class CityUpdateView(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = "update.html"
    success_url = reverse_lazy('cities')
    success_message = "City is edited successfully"


class CityDeleteView(DeleteView):
    model = City
    # template_name = 'delete.html'
    success_url = reverse_lazy('cities')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class CityListView(ListView):
    paginate_by = 100
    model = City
    template_name = 'cities.html'
