from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BookSerializer
from .models import Book
from .permissions import IsSuperuserOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication


class BookView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuserOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer
