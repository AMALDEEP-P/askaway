from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, View
from question.models import Question

from .forms import AnswerForm
from .models import Answer, UserLike

# Create your views here.


class AnswerCreateView(CreateView):
    """View for creating an answer."""

    model = Answer
    form_class = AnswerForm

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        question_id = self.request.POST.get("question_id")

        question = get_object_or_404(Question, pk=question_id)
        form.instance.user = self.request.user
        form.instance.question = question
        return super().form_valid(form)

    def form_invalid(self, form):
        question_id = self.request.POST.get("question_id")

        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{error}")

        return redirect(reverse("question:question_detail", kwargs={"pk": question_id}))

    def get_success_url(self):
        question_id = self.request.POST.get("question_id")
        return reverse("question:question_detail", kwargs={"pk": question_id})


class LikeAnswerView(LoginRequiredMixin, View):
    """View for liking an answer."""

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: like an answer.
        """
        answer_id = kwargs.get("answer_id")
        print(answer_id, kwargs)
        answer = get_object_or_404(Answer, pk=answer_id)
        user = request.user
        like, created = UserLike.objects.get_or_create(user=user, answer=answer)

        if created:
            answer.no_of_likes += 1
            answer.save()
            messages.success(request, "You liked the answer.")
        else:
            messages.error(request, "You already liked this answer.")

        return redirect(
            reverse("question:question_detail", kwargs={"pk": answer.question.id})
        )
