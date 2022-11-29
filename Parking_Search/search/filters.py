from django_filters import FilterSet, CharFilter
from .models import ParkingPlace


# создаём фильтр
class ParkingFilter(FilterSet):
    #title = CharFilter(lookup_expr='icontains')
    # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) информация о товарах
    class Meta:
        model = ParkingPlace
        fields = {'title': ['icontains'],}



    # title = CharFilter(
    #     label='Заголовок',
    #     lookup_expr='contains'  # должно быть похожее на запрос пользователя
    # )
    # # Здесь в мета классе надо предоставить модель и указать поля, по которым будет фильтроваться (т. е. подбираться) информация о товарах
    # class Meta:
    #     model = ParkingPlace
    #     fields = {'title': ['icontains'],
    #               # 'categories': ['contains']
    #               }
    #     # fields = ('title',)  # поля, которые мы будем фильтровать (т. е. отбирать по каким-то критериям, имена берутся из моделей)