from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from .models import Train
from .forms import TrainForm

__all__ = (
    'TrainDetailView',
    'TrainCreateView',
    'TrainUpdateView',
    'TrainDeleteView',
    'TrainListView',
)


class TrainListView(ListView):
    paginate_by = 100
    model = Train
    template_name = 'trains/trains.html'


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = "trains/detail.html"


class TrainCreateView(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = "trains/create.html"
    success_url = reverse_lazy('trains')
    success_message = "Train is added successfully."


class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = "trains/update.html"
    success_url = reverse_lazy('trains')
    success_message = "Train is edited successfully."


class TrainDeleteView(DeleteView):
    model = Train
    # template_name = 'delete.html'
    success_url = reverse_lazy('trains')

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Train is deleted successfully.')
        return self.post(request, *args, **kwargs)
