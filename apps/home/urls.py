from django.urls import path
from django.views.generic.base import TemplateView
from apps.home.views import home

urlpatterns = [
    path('', home, name='home'),
    # or
    # path('', TemplateView.as_view(template_name='home/home.html'), name='home'),
]