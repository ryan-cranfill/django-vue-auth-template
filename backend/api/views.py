from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .permissions import (
    AdminOrAuthorCanEdit,
)
from .models import (
    User,
    Post,
)
from .serializers import (
    UserSerializer,
    PostSerializer,
)

from .models import Message, MessageSerializer


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (
        IsAuthenticated,
    )

    @detail_route(methods=['get'])
    def posts(self, request, pk=None):
        queryset = Post.objects.filter(author__pk=pk).order_by('-created')

        context = {'request': request}

        serializer = PostSerializer(queryset, context=context, many=True)

        return Response(serializer.data)


class PostViewSet(ModelViewSet):

    queryset = Post.objects.order_by('-created')
    serializer_class = PostSerializer

    permission_classes = (
        IsAuthenticated,
        AdminOrAuthorCanEdit,
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super(PostViewSet, self).perform_create(serializer)


