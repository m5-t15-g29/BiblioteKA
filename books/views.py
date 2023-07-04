from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BookSerializer
from .models import Book
from rest_framework_simplejwt.authentication import JWTAuthentication


class BookView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = []

    queryset = Book.objects.all()
    serializer_class = BookSerializer
