"""
Question URLS
"""
from django.urls import path
from .views import QuestionListView, QuestionCreateView, QuestionDetailView

app_name = "question"

urlpatterns = [
    path("", QuestionListView.as_view(), name="question_list"),
    path("create/", QuestionCreateView.as_view(), name="question_create"),
    path("<int:pk>/", QuestionDetailView.as_view(), name="question_detail"),
]
