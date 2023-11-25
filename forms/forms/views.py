from django.shortcuts import render
from . import machine_learning_placeholder

def home(request):
    return render(request, 'index.html')


def result(request):
    user_input = request.GET['user_input']
    user_input = machine_learning_placeholder.multiplier(user_input)
    # user_input = user_input.upper()
    # user_input += " is my text!"
    return render(request, 'result.html', {'home_input': user_input})
