from django import forms
from .models import Post, Comment, Topic


# This codeblock creates a list of topics from the topic model. It goes and checkes the database for topics and adds them in a list 
# topics_list. This is afterwards added to the Post form field "topic" as a selection list. When we will add a post
# Will jhave a dropdown menu of choices on this list. 

topics = Topic.objects.all().values_list('name', 'name')
topics_list = []
for item in topics:
    topics_list.append(item)


# Form for posting 
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'content', 'author', 'status', 'expiration_date', 'topic')

        widgets = {

            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'piazza', 'type':'hidden'}),
            'topic':forms.Select(choices=topics_list, attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}), 
            # 'snippet':forms.Textarea(attrs={'class':'form-control'}),  
        }


# Form for editing a post
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'content')

        widgets = {

            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            # 'snippet':forms.Textarea(attrs={'class':'form-control'}),
        }


# Form for editing a post
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'author')

        widgets = {
            'author':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'piazza', 'type':'hidden'}),    
            'content':forms.Textarea(attrs={'class':'form-control'}),     
        }
