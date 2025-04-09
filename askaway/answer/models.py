from django.db import models

# Create your models here.


class Answer(models.Model):
    """Model for an answer."""

    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(
        "question.Question", on_delete=models.CASCADE, related_name="answers"
    )
    user = models.ForeignKey(
        "authentication.User", on_delete=models.CASCADE, related_name="answers"
    )
    is_deleted = models.BooleanField(default=False)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.answer)


class UserLike(models.Model):
    """Model for a user like."""
    user = models.ForeignKey(
        "authentication.User", on_delete=models.CASCADE, related_name="likes"
    )
    answer = models.ForeignKey(
        "answer.Answer", on_delete=models.CASCADE, related_name="likes"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + " " + str(self.answer)
