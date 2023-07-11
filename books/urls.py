from django.urls import path
from . import views
from copies.views import CopieView
from loans.views import LoanView, LoanDetailedView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("books/", views.BookView.as_view()),
    path("books/<int:pk>/", views.BookDetailView.as_view()),
    path("books/<int:pk>/follow", views.BookFollowView.as_view()),
    path("books/<int:pk>/like", views.BookLikeView.as_view()),
    path("books/<int:pk>/copies", CopieView.as_view()),
    path("books/<int:pk>/loans", LoanView.as_view()),
    path("books/<int:pk>/loans/<int:loan_id>", LoanDetailedView.as_view()),
]
