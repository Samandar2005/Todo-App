from .models import *
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.


class TodoListView(ListView):
    template_name = 'home.html'
    context_object_name = 'todo'

    def get_queryset(self):
        url_data = self.request.GET
        q = Todo.objects.all()
        if 'title' in url_data and url_data['title']:
            q = q.filter(title__icontains=url_data['title'])
        if 'description' in url_data and url_data['description']:
            q = q.filter(description__icontains=url_data['description'])
        return q


class TodoCreateView(CreateView):
    queryset = Todo.objects.all()
    template_name = 'create.html'
    fields = "__all__"

    success_url = '/todo'


class TodoUpdateView(UpdateView):
    queryset = Todo.objects.all()
    template_name = 'update.html'
    fields = "__all__"
    success_url = '/todo'


class TodoDeleteView(DeleteView):
    queryset = Todo.objects.all()
    template_name = 'delete.html'
    fields = "__all__"

    success_url = '/todo'
