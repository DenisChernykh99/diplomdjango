from django.shortcuts import render, redirect
from .models import Message


# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        text = request.POST['text']
        Message.objects.create(name=name, text=text)
        return redirect('result')
    return render(request, 'myapp/home.html', {})


def result(request):
    messages = Message.objects.all()
    return render(request, 'myapp/result.html', {'messages': messages})
