# Define urls in the accounts.

from django.urls import path, include
from . import views
app_name = 'accounts'
urlpatterns = [
    # include defaule auth urls.
    path('',include('django.contrib.auth.urls')),

    # redirecting to registration page.
    path('register/', views.register, name='register')
]