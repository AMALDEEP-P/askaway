"""
Answer URL Configuration
"""

from django.urls import path
from .views import AnswerCreateView, LikeAnswerView

app_name = "answer"

urlpatterns = [
    path("create/", AnswerCreateView.as_view(), name="answer_create"),
    path(
        "like/<int:answer_id>/",
        LikeAnswerView.as_view(),
        name="like_answer"
    ),
]
