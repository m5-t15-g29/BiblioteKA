from rest_framework import generics
from .models import Copie
from books.models import Book
from .serializers import CopieSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class CopieView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Copie.objects.all()
    serializer_class = CopieSerializer
    lookup_url_kwarg = "pk"

    def get_queryset(self):
        return Copie.objects.filter(book_id=self.kwargs["pk"])

    def perform_create(self, serializer):
        book = Book.objects.get(id=self.kwargs["pk"])
        return serializer.save(book=book)


class CopieDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Copie.objects.all()
    serializer_class = CopieSerializer
