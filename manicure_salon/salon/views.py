from django.shortcuts import render


def home(request):
    services_preview = [
        {
            'title': 'Маникюр с покрытием',
            'price': 'от 2000 ₽',
            'description': 'Аккуратная форма, обработка кутикулы, выравнивание и стойкое покрытие.',
        },
        {
            'title': 'Укрепление ногтей',
            'price': 'от 700 ₽',
            'description': 'Подходит для тонких и ломких ногтей, помогает сохранить длину.',
        },
        {
            'title': 'Дизайн ногтей',
            'price': 'от 300 ₽',
            'description': 'Френч, втирка, рисунки, стразы и минималистичный nail-art.',
        },
    ]
    advantages = [
        'Стерильные инструменты',
        'Одноразовые расходники',
        'Более 150 оттенков',
        'Уютная зона ожидания',
    ]
    return render(
        request,
        'salon/home.html',
        {'services_preview': services_preview, 'advantages': advantages}
    )


def services(request):
    services_list = [
        {
            'title': 'Классический маникюр',
            'time': '45 минут',
            'price': '1200 ₽',
            'description': 'Обработка ногтей и кутикулы, придание формы, уходовое масло.',
        },
        {
            'title': 'Маникюр с покрытием гель-лак',
            'time': '1 час 30 минут',
            'price': '2000 ₽',
            'description': 'Маникюр, выравнивание ногтевой пластины и стойкое покрытие.',
        },
        {
            'title': 'Укрепление ногтей',
            'time': '30 минут',
            'price': '700 ₽',
            'description': 'Укрепление базой или гелем для сохранения длины и формы.',
        },
        {
            'title': 'Дизайн ногтей',
            'time': '15–40 минут',
            'price': 'от 300 ₽',
            'description': 'Френч, рисунки, стразы, втирка и сезонный дизайн.',
        },
        {
            'title': 'Снятие покрытия',
            'time': '20 минут',
            'price': '500 ₽',
            'description': 'Бережное снятие старого покрытия без повреждения ногтей.',
        },
        {
            'title': 'SPA-уход для рук',
            'time': '30 минут',
            'price': '900 ₽',
            'description': 'Скраб, увлажнение, питательная маска и лёгкий массаж рук.',
        },
    ]
    return render(request, 'salon/services.html', {'services': services_list})


def masters(request):
    masters_list = [
        {
            'name': 'Анна Смирнова',
            'experience': '5 лет',
            'specialization': 'сложный дизайн, френч, тонкие линии',
            'rating': '4.9',
        },
        {
            'name': 'Мария Иванова',
            'experience': '3 года',
            'specialization': 'укрепление, нюдовые покрытия, аккуратная форма',
            'rating': '4.8',
        },
        {
            'name': 'Екатерина Орлова',
            'experience': '4 года',
            'specialization': 'SPA-уход, классический маникюр, восстановление',
            'rating': '5.0',
        },
    ]
    return render(request, 'salon/masters.html', {'masters': masters_list})


def booking(request):
    return render(request, 'salon/booking.html')


def contacts(request):
    return render(request, 'salon/contacts.html')
