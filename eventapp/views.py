from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView

from eventapp.models import Event


def index(request):
    user=request.user
    context={
        "user":user
    }
    return render(request,'events/home.html',context)

class EventDetail(DetailView):
    model = Event
    context_object_name = "event"
    template_name = "events/detail.html"

class EventView(ListView):
    queryset = Event.objects.filter(disable=False)
    template_name = "events/event.html"
    context_object_name = "events"
    paginate_by = 6

    def get_queryset(self):
        context=self.queryset
        q=self.request.GET.get("search")
        if q!='' and q is not None and q!=0:
            context=context.filter(title__icontains=q)
        return context

def election(request):
    return  render(request,'events/coming.html')


def paiement(request,slug):
    event=get_object_or_404(Event,slug=slug)
    return render(request,'events/paiement.html',context={'event':event})