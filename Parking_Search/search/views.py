from django.shortcuts import render
from datetime import datetime

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import ParkingFilter
# from .forms import AdForm, FeedbackForm
from .models import ParkingPlace
# Create your views here.

class AdrList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = ParkingPlace
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'title'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'search/adr_list.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'products'

    def get_context_data(self,
                         **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = ParkingFilter(self.request.GET,
                                          queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context

    # def get_context_data(self,
    #                      **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
    #     context = super().get_context_data(**kwargs)
    #     t = ParkingFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
    #     context['filter'] = ParkingPlace.objects.filter(name__icontains=t)
    #     return context


class Search(ListView):
    model = ParkingPlace
    template_name = 'search/search.html'
    context_object_name = 'search_list'

    # Метод get_context_data позволяет нам изменить набор данных,
    # который будет передан в шаблон.
    # def get_context_data(self, **kwargs):
    #     # С помощью super() мы обращаемся к родительским классам
    #     # и вызываем у них метод get_context_data с теми же аргументами, что и были переданы нам.
    #     # В ответе мы должны получить словарь.
    #     context = super().get_context_data(**kwargs)
    #     # К словарю добавим текущую дату в ключ 'time_now'.
    #     context['time_now'] = datetime.utcnow()
    #     # вписываем наш фильтр (AdFilter) в контекст
    #     context['filter'] = AdFilter(self.request.GET, queryset=self.get_queryset())
    #     return context
    #
    def get_queryset(self):
        queryset = super().get_queryset()
        return ParkingFilter(self.request.GET, queryset=queryset).qs
