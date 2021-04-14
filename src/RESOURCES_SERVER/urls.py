from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, LikeView, AddCommentView, AddTopicView, TopicView, TopicListView

urlpatterns = [
    
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_details'),
    path('article/<int:pk>/edit', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_topic/', AddTopicView.as_view(), name='add_topic'),
    path('topic/<str:topic>', TopicView, name='topic'),
    path('topic_list/', TopicListView, name='topic_list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/add_comment/', AddCommentView.as_view(), name='add_comment'),

]
