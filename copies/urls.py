from django.urls import path
from .views import CopieView, CopieDetailView

urlpatterns = [
    path("copies/<int:pk>/", CopieDetailView.as_view()),
]
