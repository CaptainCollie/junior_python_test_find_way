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
from find_way import views
from find_way.views import CityDetailView, CityCreateView, CityUpdateView, CityDeleteView, CityListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('cities/<int:pk>', CityDetailView.as_view(), name="detail"),
    path('cities/', CityListView.as_view(), name="cities"),
    path('add/', CityCreateView.as_view(), name='create'),
    path('update/<int:pk>', CityUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', CityDeleteView.as_view(), name='delete'),
]