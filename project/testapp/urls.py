from django.urls import path
# Импортируем созданное нами представление
from .views import ProductsList 


urlpatterns = [
   path('', ProductsList.as_view())
]