from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Note
from .forms import NoteForm
from .forms import CommentForm


class NoteListView(ListView):

    def get_queryset(self):
        tag = self.request.GET.get("tags")

        if tag:
            return Note.objects.filter(tags__contains=[tag])

        return Note.objects.all()


class NoteDetailView(DetailView, CreateView):
    template_name = 'note/note_detail.html'
    model = Note
    form_class = CommentForm

    def get_success_url(self):
        note_id = self.object.note.id
        return reverse_lazy('notes:detail', kwargs={"pk": note_id})


class NoteCreateView(CreateView):
    form_class = NoteForm
    model = Note
    success_url = reverse_lazy('notes:list')


class NoteUpdateView(UpdateView):
    form_class = NoteForm
    model = Note
    success_url = reverse_lazy('notes:list')
