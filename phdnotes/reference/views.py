from django.views.generic import View, ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Reference
from .forms import ReferenceForm


class ReferenceListView(ListView):

    def get_queryset(self):
        author = self.request.GET.get("authors")

        if author:
            return Reference.objects.filter(authors__contains=[author])

        return Reference.objects.all()


class ReferenceDetailView(DetailView):
    model = Reference


class ReferenceCreateView(CreateView):
    form_class = ReferenceForm
    model = Reference
    success_url = reverse_lazy('references:list')


class ReferenceUpdateView(UpdateView):
    form_class = ReferenceForm
    model = Reference
    success_url = reverse_lazy('references:list')
