from django.shortcuts import render
from datetime import datetime
from faker import Faker
from practapp.models import User

def my_view(request):
    # Get the current date
    current_date = datetime.now()

    # Define the context dictionary with data
    context = {
        'greeting': 'Hello, World!',
        'date': current_date,
    }

    # Render the template with the context data
    return render(request, 'practapp/index.html', context)

def user_page(request):
    
    # user = User.objects.create(first_name=first_name, last_name=last_name, email=email)
    # context = {
    #     'user': user
    # }
    user_list = User.objects.order_by("first_name")
    user_dict = {'user_page': user_list}
    return render(request, 'practapp/user.html', context=user_dict)