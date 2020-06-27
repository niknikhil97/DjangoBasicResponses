from django.urls import path,include
from .views import BookView,BookDetailView

urlpatterns = [
    path('books/', BookView.as_view()),
    path('books/<int:id>',BookDetailView.as_view()),
]
