from django.db import models

# Create your models here.


class Question(models.Model):
    """Model for a question."""

    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    user = models.ForeignKey(
        "authentication.User", on_delete=models.CASCADE, related_name="questions"
    )

    def __str__(self):
        return str(self.title)
