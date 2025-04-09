from answer.forms import AnswerForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .models import Question

# Create your views here.


class QuestionListView(ListView):
    """View for listing and creating questions."""

    model = Question
    template_name = "question/list.html"
    context_object_name = "questions"
    paginate_by = 3

    def get_queryset(self):
        """Get the questions."""

        questions = (
            Question.objects.filter(is_deleted=False)
            .prefetch_related("answers")
            .order_by("-created_at")
        )
        return questions


class QuestionCreateView(LoginRequiredMixin, CreateView):
    """View for creating a question."""

    model = Question
    template_name = "question/create.html"
    fields = ["title", "description"]
    success_url = reverse_lazy("question:question_list")
    login_url = reverse_lazy("authentication:login")

    def form_valid(self, form):
        """Set the user of the question to the current user."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class QuestionDetailView(DetailView):
    """View for displaying a question."""

    model = Question
    template_name = "question/detail.html"
    context_object_name = "question"

    def get_context_data(self, **kwargs):
        """Add the answers to the context with pagination."""
        context = super().get_context_data(**kwargs)
        answers = self.object.answers.filter(is_deleted=False).order_by("-created_at")

        paginator = Paginator(answers, 3)
        page_number = self.request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)

        context["answers"] = page_obj
        context["page_obj"] = page_obj
        context["answer_form"] = AnswerForm()
        return context


class HomeView(ListView):
    """View for the home page with list of questions."""

    model = Question
    template_name = "home/index.html"
    context_object_name = "questions"
    paginate_by = 6

    def get_queryset(self):
        """Get all non-deleted questions."""
        return (
            Question.objects.filter(is_deleted=False)
            .prefetch_related("answers")
            .order_by("-created_at")
        )
