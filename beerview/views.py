
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from .models import Beer
from .serializers import PostSerializer

class PostsList(ListCreateAPIView):
    queryset = Beer.objects.all()
    serializer_class = PostSerializer

class PostsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Beer.objects.all()
    serializer_class = PostSerializer
