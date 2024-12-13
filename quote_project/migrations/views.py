from django.shortcuts import render, redirect
from .models import Quote

def index(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/index.html', {'quotes': quotes})

def add_quote(request):
    if request.method == 'POST':
        text = request.POST['text']
        author = request.POST['author']
        Quote.objects.create(text=text, author=author)
        return redirect('index')
    return render(request, 'quotes/add_quote.html')
