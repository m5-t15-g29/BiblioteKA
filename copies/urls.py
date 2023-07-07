from django.urls import path
from .views import CopieListCreateView, CopieRetrieveUpdateDestroyView

urlpatterns = [
    path("copies/", CopieListCreateView.as_view()),
    path("copies/<int:pk>/", CopieRetrieveUpdateDestroyView.as_view()),
]
