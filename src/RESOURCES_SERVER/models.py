# RESOURCE SERVER MODELS FILE
# ---------------------------------------------------------------------------------
from datetime import datetime, date 
from django.db import models
from django.utils import timezone 
from django.urls import reverse 
from django.contrib.auth.models import User

from PIAZZA_API.settings import OAUTH2_PROVIDER

# Importing the validator libraries
from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# This will help us use Rich text in our blog (We first installed ck editor, installation command: pip install django-ckeditor)
from ckeditor.fields import RichTextField

# Importing the timeuntil  template filt
from django.utils.timesince import timeuntil

# ----------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------

# from datetime import datetime, timezone



# this is the tokens expire time from the Auth2 system. We have imported it from the settings
token_expire_time = OAUTH2_PROVIDER['ACCESS_TOKEN_EXPIRE_SECONDS']

token_expire_time_datetime_converted = datetime.fromordinal(token_expire_time)



# Model for the topic resource.
# This model has been created for having the topics as objects in our database in order to create new topics for our posts and be able to 
# manage them in the future. This was hardcoded inside the Post model class as a list of coices for our topics initialy but we created a 
# model to handle the associations with the post and User models and for the topics list to be more dynamic. 
# We have added a feature in the PIAZZA web site of adding a new topic.
# ----------------------------------------------------------------------------------------------------------------------------------------
class Topic(models.Model): 

    name = models.CharField(max_length=100)
    
    def __str__(self):
        return  self.name


    def get_absolute_url(self):
        return reverse('home')
    




# Here we create a list of topics. Everytime a topic is created it is getting added to the topics_list 
# and  we pass that list as choices ot our "Post" model "topic" field. 
topics = Topic.objects.all().values_list('name', 'name')

topics_list = []

for item in topics:
    topics_list.append(item)




# Model for the posts 
# ----------------------------------------------------------------------------------------------------------------------------------------
class Post(models.Model): 

    """
    # Validator for Post to be unique by title. If we have 2 posts with the same title we will get a validation error message
    def validate_unique(value):
        data = Post.objects.all()
        for element in data:
            if str(value) == str(element):
                raise ValidationError(_('The post with title "%(value)s" already exist'), params = {'value': value},)
    
    
    # Validator for Post expiration time. This is Set by user but we can set a max expire time and prompting users to add a smaller expire time.
    def set_max_expire_time(value):
            print('The maximum expiration time for the post is 3600. If ')
            if value>=3600: # just by changing this value here in our if statement we can set the max expire time for our post.
                raise ValidationError(_('The expiration time "%(value)s" you have set for the post is more than 3600 seconds. Please insert a expire time less than 3600 seconds.'), params = {'value': value},)

    """

    STATUS = (
        ('LIVE', 'LIVE'),
        ('EXPIRED', 'EXPIRED'),
    )

    
    title = models.CharField(max_length=100)                                                #<--------  Post title | Using a validator here to check if post title is unique
    title_tag = models.CharField(max_length=255, default='')                                #<--------  Post title_tag (labe this will show on the web browser tab)
    topic = models.CharField(max_length=100, choices=topics_list)                           #<--------  Post topic is a field that is a model itself and categorises the post to a topic...
    date = models.DateTimeField(default=timezone.now)                                       #<--------  Post date creation
    expiration_date = models.DateTimeField(default=timezone.now)                            #<--------  Post expiration date
    content = RichTextField(blank=True, null=True)                                          #<--------  Post content                                                                   
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True )      #<--------  Post author - User that created the post
    status = models.CharField(max_length=7, choices=STATUS, default="LIVE")                 #<--------  Post status (expired or not expired)
    snippet = models.CharField(max_length=100)                                              #<--------  Post snipet (we can add this and will show in the main page)
    likes = models.ManyToManyField(User, related_name='likes')                              #<--------  Post likes
    
    
    # Functions that returs the status of a post 
    # LIVE if the ost is still active and EXPIRED if post has expired.
    def post_status(self):
        if self.expiration_date > timezone.now():
            new_status = "LIVE"
            return new_status
        else:
            new_status = "EXPIRED"
            return new_status

    # Function that returns the total number of likes in a post
    def total_likes(self):
        return self.likes.count()

    #this is a function to return us to the home page of our web app.
    def get_absolute_url(self):
        return reverse('home')
    
    # This class is used to order the posts by date. Latest post appears 1st.
    class Meta:
        ordering = ['-date']
    
    # Dajango admin: how does a post shows in the admin panel. (Post title | post author )
    def __str__(self):
        return str(self.id) + ' | ' + self.title + ' | ' + str(self.author) 
    



# Model for the comments
# ----------------------------------------------------------------------------------------------------------------------------------------
class Comment(models.Model): 

    post = models.ForeignKey(Post, related_name="post_comment", on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, related_name="author_comment", on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('home')
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return 'Comment: ' + str(self.id) + ' | Post id:' + str(self.post.id) + ' | This comment was created by: ' + str(self.author) + ' | on the post: ' + str(self.post.title)




# Model for the user profiles
# Created that profile model for the users profile in order to be able to edit  and update a users profile. 
# This has not been properly developed yet. It has just been created for  future website development.
# It has only 2 fiels at the moment the user which is a one to on field with the authenticated User and has a bio text field to write users bio. 
# more fields to be added in the future.
# ----------------------------------------------------------------------------------------------------------------------------------------
class Profile(models.Model): 


    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str_(self):
        return str(self.user)