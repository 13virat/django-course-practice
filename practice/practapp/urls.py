from django.urls import path
from practapp import views

urlpatterns = [
    path('', views.user_page, name='user_page')
]
