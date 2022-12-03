from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from eventapp.models import Event


def index(request):
    user=request.user
    context={
        "user":user
    }
    return render(request,'events/home.html',context)

class EventView(ListView):
    model = Event
    template_name = "events/event.html"
    context_object_name = "events"
