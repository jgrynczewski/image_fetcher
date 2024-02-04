from django import views
from django.shortcuts import render, redirect

from accounts.forms import SignUpForm, SignInForm


class SignUp(views.View):
    def get(self, request):
        form = SignUpForm()

        return render(
            request,
            'accounts/signup.html',
            context={
                'form': form
            }
        )

    def post(self, request):
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('accounts:signin')

        return render(
            request,
            'accounts/signup.html',
            context={
                'form': form
            }
        )


class SignIn(views.View):
    def get(self, request):
        form = SignInForm()

        return render(
            request,
            'accounts/signin.html',
            context={
                'form': form
            }
        )
