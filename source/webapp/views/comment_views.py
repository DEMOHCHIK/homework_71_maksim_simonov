from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from ..models import Comment, Publication


class CommentCreateView(CreateView):
    model = Comment
    fields = ['text']
    template_name = 'comment/comment_create.html'
    success_url = reverse_lazy('webapp:publication_view')

    def form_valid(self, form):
        form.instance.publication = Publication.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        publication_pk = self.kwargs['pk']
        return reverse('webapp:publication_view', kwargs={'pk': publication_pk})


class CommentDeleteView(DeleteView):
    model = Comment

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:publication_view', kwargs={'pk': self.object.publication.pk})
