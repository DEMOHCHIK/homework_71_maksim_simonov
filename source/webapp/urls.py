from django.urls import path
from webapp.views.publication_views import HomeView, PublicationCreateView, LikePostView

app_name = 'webapp'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('publications/create/', PublicationCreateView.as_view(), name='publication_create'),
    path('publications/<int:pk>/like', LikePostView.as_view(), name='publication_like'),
]
