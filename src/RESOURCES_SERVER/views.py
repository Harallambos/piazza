# RESOURCES SERVER VIEWS FILE
# ------------------------------------------------------------------------------------------------------------------------
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from oauth2_provider.views.generic import ProtectedResourceView

import requests

from AUTH_SERVER.serializers import CreateUserSerializer

# ------------------------------------------------------------------------------------------------------------------------
from django.shortcuts import render
from rest_framework import viewsets
from .models import Post, Comment , Topic
from .serializers import PostSerializer, CommentSerializer , TopicSerializer
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponseRedirect

# ------------------------------------------------------------------------------------------------------------------------
# The following imports are from the piazza website
# ------------------------------------------------------------------------------------------------------------------------

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse

# -----------------------------------------------------------------------------------------------------------------------------
# The Following fields are the client id and the Client secret when we go and create an application for our api
# plese  visit  URL: http://10.61.64.32:8000/o/applications/
# We have created an application called PIAZZA and if you click on it the cliend id and client secret will appear there and we have to add them to the following variables.
# These can be also found in the django admin page.

CLIENT_ID = '8RPubhMrs7GZHVrFe4AvcTAXAvCFOJFyvwHKhZQH'
CLIENT_SECRET = '2coWq1bb0cnP4zviaH4E7aKQNJXicKetQUaoaYNsivNODeesP80PughOWU86phlv35gZAx843fd3nOp9rDld5MAYdKfGrW83AZKGNKD472lU6CAzSgGJVKonFNvFnQwB'

IP_token = 'http://10.61.64.32:8000/o/token/'
IP_revoke_token ='http://10.61.64.32:8000/o/revoke_token/'
# -------------------------------------------------------------------------------------------------------------------------------




# VIEWS CLASESS FOR OUR PIAZZA API ENDPOINTS
#--------------------------------------------------------------------------------------------------------------------

# Class por the post view: http://10.61.64.32:8000/api/post
class PostViewSet(viewsets.ModelViewSet): 
    """
    Registers user to the server. Input should be in the format:

    {     
        "title":"title",

        "topic":"Politics | Health | Sport | Tech",

        "content":"content",

        "expiration_date":"yyyy-mm-dd hh:mm:ss",

        "author":"user id", 
    }
    
    API URL: http://10.61.64.32:8000/api/post/
    to see the API functionality.
    """
    queryset = Post.objects.all() 
    serializer_class = PostSerializer


# Class por the comment view: http://10.61.64.32:8000/api/comment
class CommentViewSet(viewsets.ModelViewSet): 
    """
    Adds a comment on a post. Input should be in the format:

    { 
        "post": "title", 

        "content":"content", 

    }
    
    API URL: http://10.61.64.32:8000/api/comment/
    """
    queryset = Comment.objects.all() 
    serializer_class = CommentSerializer



# Class por the topic view: http://10.61.64.32:8000/api/topic
class TopicViewSet(viewsets.ModelViewSet): 
    """
    Adds a comment on a post. Input should be in the format:
    
    {
        "name":"name", 
    }
    
    API URL: http://10.61.64.32:8000/api/topic/
    """
    queryset = Topic.objects.all() 
    serializer_class = TopicSerializer









# VIEWS CLASESS FOR OUR PIAZZA WEB SITE ENDPOINTS
#--------------------------------------------------------------------------------------------------------------------



# class for our web site home page: http://10.61.64.32:8000/
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    topic = Topic.objects.all()
    ordering = ['-date']

    
    def get_context_data(self, *args, **kwargs):
        topic_menu = Topic.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["topic_menu"] = topic_menu
        return context
    


# This is the class for our web site a post details: http://10.61.64.32:8000/article/7  #<----- needs to have the post id at the end
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'         

    def get_context_data(self, *args, **kwargs):
        topic_menu = Topic.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes() # <------------ Calling the "total_likes" function from our models.py file for the "Post" model
        post_status = stuff.post_status()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["topic_menu"] = topic_menu
        context["total_likes"] = total_likes
        context["post_status"] = post_status
        context["liked"] = liked
        return context




# class for our web site add_post.html page: http://10.61.64.32:8000/add_post/
class AddPostView(CreateView):
    model= Post
    form_class = PostForm
    template_name = 'add_post.html'


# class for our web site add_comment.html page: http://10.61.64.32:8000/article/8/add_comment/
class AddCommentView(CreateView):
    model= Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')
    # fields = '__all__'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


# class for our web site update_post.html page: http://10.61.64.32:8000/article/7/edit  #<----- needs to have the post id at the end as we edit a specific post
class UpdatePostView(UpdateView):
    model= Post
    form_class = EditForm
    template_name = 'update_post.html'



# class for our web site delete_post.html page: http://10.61.64.32:8000/article/7/delete  #<----- needs to have the post id at the end as we delete a specific post
class DeletePostView(DeleteView):
    model= Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


# class for our web site add_topic.html page: http://10.61.64.32:8000/add_topic/
class AddTopicView(CreateView):
    model= Topic
    template_name = 'add_topic.html'
    fields = '__all__'


def TopicView(request, topic):
    topic_post = Post.objects.filter(topic=topic.replace('-', ' '))
    return render(request, 'topic.html', { 'topic':topic.title().replace('-', ' '), 'topic_post':topic_post })


# Function view for our web site topic_list.html page: http://10.61.64.32:8000/topic_list/
# NOT WORKING AT THE MOMENT 
def TopicListView(request):
    topic_menu_list = Topic.objects.all()
    return render(request, 'topic_list.html', {'topic_menu_list': topic_menu_list})


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse('article_details', args=[str(pk)]))
