from django.shortcuts import render


def home(request):
    services_preview = [
        {'title': 'Маникюр с покрытием', 'price': '2000 ₽'},
        {'title': 'Классический маникюр', 'price': '1200 ₽'},
        {'title': 'Дизайн ногтей', 'price': 'от 300 ₽'},
    ]
    return render(request, 'salon/home.html', {'services_preview': services_preview})


def services(request):
    services_list = [
        {'title': 'Классический маникюр', 'time': '45 минут', 'price': '1200 ₽', 'description': 'Аккуратная обработка ногтей и кутикулы без покрытия.'},
        {'title': 'Маникюр с покрытием гель-лак', 'time': '1 час 30 минут', 'price': '2000 ₽', 'description': 'Маникюр, выравнивание и стойкое покрытие.'},
        {'title': 'Укрепление ногтей', 'time': '30 минут', 'price': '700 ₽', 'description': 'Укрепление натуральных ногтей базой или гелем.'},
        {'title': 'Дизайн ногтей', 'time': '15–40 минут', 'price': 'от 300 ₽', 'description': 'Френч, рисунки, стразы, втирка и другие варианты дизайна.'},
        {'title': 'Снятие покрытия', 'time': '20 минут', 'price': '500 ₽', 'description': 'Бережное снятие старого покрытия.'},
        {'title': 'SPA-уход для рук', 'time': '30 минут', 'price': '900 ₽', 'description': 'Увлажнение, скраб и питательная маска для кожи рук.'},
    ]
    return render(request, 'salon/services.html', {'services': services_list})


def masters(request):
    masters_list = [
        {'name': 'Анна Смирнова', 'experience': '5 лет', 'specialization': 'сложный дизайн и френч'},
        {'name': 'Мария Иванова', 'experience': '3 года', 'specialization': 'укрепление и аккуратное покрытие'},
        {'name': 'Екатерина Орлова', 'experience': '4 года', 'specialization': 'SPA-уход и классический маникюр'},
    ]
    return render(request, 'salon/masters.html', {'masters': masters_list})


def booking(request):
    return render(request, 'salon/booking.html')


def contacts(request):
    return render(request, 'salon/contacts.html')
