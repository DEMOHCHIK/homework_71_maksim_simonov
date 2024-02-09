from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from ..models import Comment, Publication


class CommentCreateView(CreateView):
    model = Comment
    fields = ['text']
    success_url = reverse_lazy('publication_view')

    def form_valid(self, form):
        form.instance.publication = Publication.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)


class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy('publication_view')
