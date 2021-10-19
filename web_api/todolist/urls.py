from django.urls import path
from .views import TodoListView


urlpatterns = [
  path('todos/', TodoListView.as_view()),
  path('todos/<int:pk>/', TodoListView.as_view()),
]