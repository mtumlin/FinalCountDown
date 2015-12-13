from django.views import generic
from countdown.models import Event
from datetime import datetime


class IndexView(generic.ListView):
    context_object_name = 'list_of_events'
    template_name = 'countdown/index.html'

    def get_queryset(self):
        return Event.objects.filter(date__gt=datetime.now())


class DetailView(generic.DetailView):
    model = Event
    template_name = 'countdown/detailed.html'
