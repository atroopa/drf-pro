from rest_framework.generics import ListAPIView
from blog.models import Article
from .serializers import ArticleSerializer

# Create your views here.
class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer