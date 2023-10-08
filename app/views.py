from rest_framework import generics
from .models import Post
from rest_framework.permissions import AllowAny
from .serializers import PostSerializer


class PostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # ログインユーザー以外がアクセスできるようにするためのpermission設定
    permission_classes = (AllowAny,) 


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # ログインユーザー以外がアクセスできるようにするためのpermission設定
    permission_classes = (AllowAny,)