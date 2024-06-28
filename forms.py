from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

USER_TYPE_CHOICES = [
    ('admin', 'Admin'),
    ('doctor', 'Doctor'),
    ('user', 'patient'),
]

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2", "user_type")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.user_type = self.cleaned_data["user_type"]
        if commit:
            user.save()
        return user
