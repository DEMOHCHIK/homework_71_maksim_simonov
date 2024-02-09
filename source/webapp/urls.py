from django.urls import path
from webapp.views import HomeView, PublicationCreateView, LikePostView, PublicationView, CommentCreateView, CommentDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('publications/create/', PublicationCreateView.as_view(), name='publication_create'),
    path('publication/<int:pk>/', PublicationView.as_view(), name='publication_view'),
    path('publication/<int:pk>/comment/create/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('publications/<int:pk>/like', LikePostView.as_view(), name='publication_like'),

]
