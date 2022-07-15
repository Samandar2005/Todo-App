from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', TodoListView.as_view(), name='todo-create'),
    path('todo', TodoListView.as_view()),
    path('todo/add', TodoCreateView.as_view(), name='todo-create'),
    path('todo/update/<int:pk>',
         TodoUpdateView.as_view(), name='todo-update'),
    path('todo/delete/<int:pk>',
         TodoDeleteView.as_view(), name='todo-delete'),
]
