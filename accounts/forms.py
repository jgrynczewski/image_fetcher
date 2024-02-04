from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField


User = get_user_model()


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label='Hasło',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text='',
    )
    password2 = forms.CharField(
        label='Powtórz hasło',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text='',
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )
        labels = {
            'username': 'Nazwa użytkownika',
            'email': 'Email',
        }
        help_texts = {
            'username': ''
        }


class SignInForm(AuthenticationForm):
    password = forms.CharField(
        label='Hasło',
        strip=False,
        widget=forms.PasswordInput(),
    )
    username = UsernameField(label='Username')
