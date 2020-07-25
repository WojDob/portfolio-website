import random

from django.shortcuts import render


# Create your views here.
def home_view(request):
    num = random.randint(1, 100)
    some_list = [
        random.randint(1, 100000),
        random.randint(1, 100000),
        random.randint(1, 100000),
    ]
    context = {
        'bool_item': True, 
        'num': num,
        'some_list': some_list,
    }
    return render(request, 'myapp/index.html', context)


def contact_view(request):
    return render(request, 'myapp/contact.html')


def about_view(request):
    mytech = [
        {
          'name': 'HTML',
          'url': 'https://www.w3schools.com/html/',
          'level': 'beginner'
        },
        {
          'name': 'CSS',
          'url': 'https://www.w3schools.com/css/',
          'level': 'beginner'
        },
        {
          'name': 'Bootstrap 4',
          'url': 'https://getbootstrap.com',
          'level': 'beginner'
        },
        {
          'name': 'Python',
          'url': 'https://www.python.org',
          'level': 'intermediate'
        },
        {
          'name': 'Django',
          'url': 'https://www.djangoproject.com',
          'level': 'beginner'
        },    
    ]
    context = {
      'lucky_num': random.randint(1, 10),
      'unlucky_num': random.randint(1, 10),
      'mytech': mytech
    }
    return render(request, 'myapp/about.html', context)