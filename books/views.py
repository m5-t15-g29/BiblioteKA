from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)
from .serializers import BookSerializer, BooksLikesSerializer, BooksUserSerializer
from .models import Book, BooksLikes, BooksUser
from .permissions import IsSuperuserOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


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


class BookFollowView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = BooksUserSerializer

    def perform_create(self, serializer):
        book = Book.objects.get(id=self.kwargs["pk"])
        return serializer.save(book=book, user=self.request.user)


class BookLikeView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = BooksLikesSerializer

    def perform_create(self, serializer):
        book = Book.objects.get(id=self.kwargs["pk"])
        return serializer.save(book=book, user=self.request.user)
