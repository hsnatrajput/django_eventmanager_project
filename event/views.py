
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from .models import Event
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm 

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('event_list')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'


class EventCreateView(CreateView):
    model = Event
    fields = ['title', 'description', 'date', 'time', 'organizer']
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event_list')



class EventUpdateView(UpdateView):
    model = Event
    fields = ['title', 'description', 'date', 'time', 'organizer']
    template_name = 'events/event_form.html'
    success_url = reverse_lazy('event_list')


class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('event_list')

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'
