from django.shortcuts import render

def platform(request):
    return render(request, 'fourth_task/home.html')

def game(request):
    game_dict = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 77"]}
    context = {
        'game_dict': game_dict,
    }
    return render(request, 'fourth_task/shop.html', context)

def shopping_cart(request):
    return render(request, "fourth_task/shopping_cart.html")

