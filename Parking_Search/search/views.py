# from django.shortcuts import render
# from datetime import datetime
#
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#
# from .filters import AdFilter, FeedbackFilter
# from .forms import AdForm, FeedbackForm
# from .models import ParkinrPlace
# # Create your views here.
#
# class Search(ListView):
#     model = ParkinrPlace
#     template_name = 'ads/search.html'
#     context_object_name = 'search_list'
#
#     # Метод get_context_data позволяет нам изменить набор данных,
#     # который будет передан в шаблон.
#     def get_context_data(self, **kwargs):
#         # С помощью super() мы обращаемся к родительским классам
#         # и вызываем у них метод get_context_data с теми же аргументами, что и были переданы нам.
#         # В ответе мы должны получить словарь.
#         context = super().get_context_data(**kwargs)
#         # К словарю добавим текущую дату в ключ 'time_now'.
#         context['time_now'] = datetime.utcnow()
#         # вписываем наш фильтр (AdFilter) в контекст
#         context['filter'] = AdFilter(self.request.GET, queryset=self.get_queryset())
#         return context
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return AdFilter(self.request.GET, queryset=queryset).qs
