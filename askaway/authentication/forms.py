from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

User = get_user_model()


class SignUpForm(forms.ModelForm):
    """Form for creating a new user account with strong password validation."""

    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        """Meta class for the SignUpForm."""

        model = User
        fields = ["username", "email", "password", "confirm_password"]
        widgets = {
            "password": forms.PasswordInput(),
        }

    def clean_password(self):
        """Validate password strength."""
        password = self.cleaned_data.get("password")
        try:
            validate_password(password, self.instance)
        except ValidationError as error:
            raise ValidationError(list(error.messages))

        return password

    def clean(self):
        """Validate that the two password fields match."""
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords don't match")

        return cleaned_data

    def save(self, commit=True):
        """Saves the new user account."""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        return user
