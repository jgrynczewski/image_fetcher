from django.urls import path

from fetch_app import views

app_name = 'fetch_app'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
]