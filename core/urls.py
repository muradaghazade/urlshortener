from django.urls import path
from core.views import home, redirect_view

app_name = 'core'

urlpatterns = [
    path('', home, name ='main'),
    path('<str:code>', redirect_view, name='redirect'),
]