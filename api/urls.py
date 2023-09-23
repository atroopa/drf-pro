from django.urls import path , include
from .views import ArticleListView, ArticleDetail, UserListView, UserDetail

app_name = "api"

urlpatterns = [
    path("", ArticleListView.as_view(), name="list"),
    path("<int:pk>", ArticleDetail.as_view(), name="detail"),
    path("users", UserListView.as_view(), name="user_list"),
    path("users/<int:pk>", UserDetail.as_view(), name="user_detail"),
]