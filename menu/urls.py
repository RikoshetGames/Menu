from django.urls import path

from menu.apps import MenuConfig
from menu.views import MenuView

app_name = MenuConfig.name

urlpatterns = [
    path('', MenuView.as_view(), name='menu'),
    ]