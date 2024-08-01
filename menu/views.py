from django.shortcuts import render
from django.views.generic import ListView

from menu.models import Menu


# Create your views here.


class MenuView(ListView):
    model = Menu

    def get(self, request):
        menu = Menu.objects.all()
        return render(request, 'menu/menu.html', {'menu_items': menu})