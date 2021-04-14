"""PIAZZA_API URL Configuration
# -----------------------------------------------------------------------------

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include



# This is are the url's for our API viewsets
###################################################################################################

from rest_framework.routers import DefaultRouter
from RESOURCES_SERVER.views import PostViewSet, CommentViewSet , TopicViewSet
router = DefaultRouter()

# This will be the URL for our API endpoint for the posts   http://10.61.64.32:8000/api/post
router.register('post', PostViewSet)

# This will be trhe url for our API endpoint for comments    http://10.61.64.32:8000/api/comment
router.register('comment', CommentViewSet)

# This will be the URL for our API endpoint for the posts   http://10.61.64.32:8000/api/topic
router.register('topic', TopicViewSet)

###################################################################################################


urlpatterns = [
    
    # This will be our django admin page url http://10.61.64.32:8000/admin
    path('admin/', admin.site.urls),

    # PIAZZA website urls for home page and for registering members on the website
    # http://10.61.64.32:8000/article/<int:pk>
    # http://10.61.64.32:8000/article/<int:pk>/edit
    # http://10.61.64.32:8000/article/<int:pk>/delete
    # http://10.61.64.32:8000/article/add_post
    path('', include('RESOURCES_SERVER.urls')),
    
     
    # We just created a new URL in the form http://10.61.64.32:8000/o where o is the resource for performing the authentication phase (“o” for “oAuth”).
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')), 
    
    # The Authorosation server api url endpoints are on the AUTH_SERVER.urls.py file
    # http://10.61.64.32:8000/auth/register/
    # http://10.61.64.32:8000/auth/token/
    # http://10.61.64.32:8000/auth/token/refresh/
    # http://10.61.64.32:8000/auth/token/revoke/
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('AUTH_SERVER.urls')),
    
    
    # These will be our root API url :                           http://10.61.64.32:8000/api
    # This will be trhe url for our API endpoint for posts       http://10.61.64.32:8000/api/post
    # This will be trhe url for our API endpoint for comments    http://10.61.64.32:8000/api/comment
    # This will be trhe url for our API endpoint for likes       http://10.61.64.32:8000/api/like
    path('api/', include(router.urls)),
    

]





