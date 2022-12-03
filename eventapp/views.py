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
    queryset = Event.objects.filter(disable=False)
    template_name = "events/event.html"
    context_object_name = "events"
    paginate_by = 1

    def get_queryset(self):
        context=self.queryset
        q=self.request.GET.get("search")
        if q!='' and q is not None and q!=0:
            context=context.filter(title__icontains=q)
        return context

def election(request):
    return  render(request,'events/coming.html')
