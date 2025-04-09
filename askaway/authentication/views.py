from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import SignUpForm

User = get_user_model()


class CustomLoginView(LoginView):
    """
    Extends the default Django LoginView to use a custom template.
    """

    template_name = "authentication/login.html"


class SignUpView(CreateView):
    """
    Creates a new user account.
    """

    model = User
    form_class = SignUpForm
    template_name = "authentication/signup.html"
    success_url = reverse_lazy("authentication:login")

    def form_valid(self, form):
        """Add success message on valid form submission."""
        response = super().form_valid(form)
        messages.success(
            self.request,
            "Your account has been created successfully! Please log in with your credentials.",
        )
        return response


# Create your views here.
