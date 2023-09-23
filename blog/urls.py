from django.urls import path , include
from .views import ArticleList, ArticleDtail

urlpatterns = [
    path("", ArticleList.as_view(), name='list'),
    path("<int:pk>", ArticleDtail.as_view(), name='detail'),
]