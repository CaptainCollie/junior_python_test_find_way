"""junior_python_test_find_way URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import ways.views
from find_way import views
from find_way.views import CityDetailView, CityCreateView, CityUpdateView, CityDeleteView, CityListView
from trains.views import TrainDetailView, TrainListView, TrainCreateView, TrainUpdateView, TrainDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cities/<int:pk>', CityDetailView.as_view(), name="detail"),
    path('cities/', CityListView.as_view(), name="cities"),
    path('add/', CityCreateView.as_view(), name='create'),
    path('update/<int:pk>', CityUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', CityDeleteView.as_view(), name='delete'),
    path('trains/<int:pk>', TrainDetailView.as_view(), name="detailtr"),
    path('trains/', TrainListView.as_view(), name="trains"),
    path('addtr/', TrainCreateView.as_view(), name='createtr'),
    path('updatetr/<int:pk>', TrainUpdateView.as_view(), name='updatetr'),
    path('deletetr/<int:pk>', TrainDeleteView.as_view(), name='deletetr'),
    path('ways/', ways.views.home, name='ways'),
    path('find_way/', ways.views.find_way, name='find_way')
]
