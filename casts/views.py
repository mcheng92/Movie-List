from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .form import CastForm
from .models import Casts, Movie

# Create your views here.


class CastList(ListView):
    model = Casts
    template_name = "cast-index.html"
    context_object_name = "casts"


class CastDetail(DetailView):
    model = Casts
    template_name = "cast-detail.html"
    context_object_name = "cast"


class CastCreate(CreateView):
    model = Casts
    form_class = CastForm
    template_name = "add-cast.html"
    success_url = reverse_lazy('cast-index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies_exist'] = Movie.objects.exists()
        return context
    
    def form_valid(self, form):
        form.instance.character = form.cleaned_data['character'].strip().lower().title()
        form.instance.actor = form.cleaned_data['actor'].strip().lower().title()
        return super().form_valid(form)

class CastUpdate(UpdateView):
    model = Casts   
    template_name = "edit-cast.html"
    success_url = reverse_lazy('cast-index')
    fields = '__all__'

class CastDelete(DeleteView):
    model = Casts
    template_name = "delete-cast.html"
    success_url = reverse_lazy('cast-index')