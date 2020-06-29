from django.urls import path,include,re_path
from .views import BookView,BookDetailView

urlpatterns = [
    path('books/', BookView.as_view()),
    re_path(r'^books/(?P<id>\d+)',BookDetailView.as_view()),
]
