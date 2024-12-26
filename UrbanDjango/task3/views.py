from django.shortcuts import render
from django.views.generic import TemplateView

def platform(request):
    return render(request, 'Home.html')

def shop(request):
    return render(request, 'shop.html')

def shopping_cart(request):
    return render(request, 'shopping_cart.html')


def game(request):
    game_1 = 'Atomic Heart'
    game_2 = 'Cyberpank 2077'
    game_3 = 'PayDay 2'
    context = {
        'game_1': game_1,
        'game_2': game_2,
        'game_3': game_3,
    }
    return render(request,'shop.html', context)
# Create your views here.
