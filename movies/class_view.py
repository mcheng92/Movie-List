from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import MovieForm 
from .models import Movie

class HomeView(TemplateView):
    template_name = 'home.html'

class MovieList(ListView):
    model = Movie
    template_name = 'index.html'
    context_object_name = 'movies'
    success_url = reverse_lazy('home')

class MovieDetail(DetailView):
    model = Movie
    template_name = 'detail.html'
    context_object_name = 'movie'
    success_url = reverse_lazy('index')
    

class MovieCreate(CreateView):
    model = Movie
    template_name = 'add.html'
    fields = MovieForm.Meta.fields
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.instance.name = form.cleaned_data['name'].strip().lower().title()
        form.instance.genres = form.cleaned_data['genres'].strip().lower().title()
        return super().form_valid(form)

class MovieUpdate(UpdateView):
    model = Movie
    template_name = 'edit.html'
    fields = MovieForm.Meta.fields
    success_url = reverse_lazy('index')

class MovieDelete(DeleteView):
    model = Movie
    template_name = 'delete.html'
    success_url = reverse_lazy('index')
