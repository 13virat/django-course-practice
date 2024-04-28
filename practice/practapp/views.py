from django.shortcuts import render
from datetime import datetime

# from practapp.models import User
from .forms import NewUserForm

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
    
    
    # user_list = User.objects.order_by("first_name")
    # user_dict = {'user_page': user_list}
    # return render(request, 'practapp/user.html', context=user_dict)
    form=NewUserForm()
    if request.method=='POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return my_view(request)
        else:
            print("ERROR FORM INVALID")
    return render(request, 'practapp/user.html', {'form': form})        