from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer
from django.contrib.auth.models import User
from .permissions import IsSuperUser, IsAuthorOReadOnly, IsStaffOrReadonly

# Create your views here.
class ArticleListView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsStaffOrReadonly, IsAuthorOReadOnly)

class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class UserListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)