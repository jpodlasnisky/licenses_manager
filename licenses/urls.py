from django.urls import path
from .views import index, valida

urlpatterns = [
    path('', index, name='index'),
    path('valida', valida, name='valida')
]
