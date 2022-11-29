from django.urls import path
from .views import Search, AdrList

urlpatterns = [
    # Представляем наш класс списка объявлений(AdvertisementList из view.py) при помощи метода as_view.
    path('', AdrList.as_view(), name='adresses_list'),
    path('search', Search.as_view(), name='search_list'),
]