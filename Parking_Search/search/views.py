from django.views.generic import ListView
from .filters import ParkingFilter
from .models import ParkingPlace
# Create your views here.

from django.contrib.postgres.search import SearchVector, SearchQuery, SearchHeadline
from django.contrib.postgres.search import TrigramSimilarity
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

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        qu = self.request.GET
        qs = ParkingPlace.objects.annotate(search=SearchVector("title")).filter(search=SearchQuery(qu))
        context['filter'] = ParkingFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        context['queryset'] = qs
        return context

class Search(ListView):
    model = ParkingPlace
    template_name = 'search/search.html'
    context_object_name = 'search_list'

    # Метод get_context_data позволяет нам изменить набор данных,
    # который будет передан в шаблон.
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами, что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        qs = ParkingPlace.objects.all()
        query = self.request.GET.get("query")
        if query:
            #qs = Post.objects.filter(title__icontains=query)
            #qs = ParkingPlace.objects.annotate(search=SearchVector("title")).filter(search=SearchQuery(query))
            qs = ParkingPlace.objects.filter(title__icontains=query).annotate(
                headline=SearchHeadline(
                    "title",
                    SearchQuery(query),
                    start_sel="<b><u><i>",
                    stop_sel="</i></u></b>",
                )
            )
        # similar = ParkingPlace.objects.filter(
        #         title__trigram_word_similar=query,
        #     ).annotate(word_similarity=TrigramWordSimilarity(query, "title"),
        #     ).values("title", "word_similarity").order_by("-word_similarity")
        qst = ParkingPlace.objects.all()
        similar = ParkingPlace.objects.filter(
            title__trigram_similar=query,
        ).annotate(similarity=TrigramSimilarity("title", query)).order_by("-similarity"),
        context['search_res'] = qs
        context['search_sim'] = similar
        return context



