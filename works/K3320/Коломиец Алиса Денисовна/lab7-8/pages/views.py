from django.shortcuts import render
from django.contrib import messages
from .models import Feedback

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Сохраняем данные в базу
        Feedback.objects.create(name=name, email=email, message=message)
        
        # Добавляем сообщение об успехе
        messages.success(request, 'Ваше сообщение успешно отправлено!')
        
        # Можно добавить перенаправление, чтобы избежать повторной отправки формы
        # return redirect('contact')
    
    return render(request, 'pages/contact.html')