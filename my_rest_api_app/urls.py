from django.urls import path
from my_rest_api_app import views

urlpatterns = [
    path('', views.UserList.as_view()),
]