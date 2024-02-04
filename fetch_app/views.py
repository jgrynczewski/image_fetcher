from django import views
from django.shortcuts import render


class HomeView(views.View):
    def get(self, request):
        return render(
            request,
            'fetch_app/home.html'
        )