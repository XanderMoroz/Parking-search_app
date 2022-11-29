from django.views.generic import ListView
from .models import ParkingPlace
# Create your views here.

from django.contrib.postgres.search import SearchVector, SearchQuery, SearchHeadline
# from django.contrib.postgres.search import TrigramSimilarity

class Search(ListView):
    model = ParkingPlace
    template_name = 'search/search.html'
    context_object_name = 'search_list'

    # Метод get_context_data позволяет нам изменить набор данных, который будет передан в шаблон.
    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами, что и были переданы нам.
        context = super().get_context_data(**kwargs)
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
        context['search_res'] = qs
        return context



