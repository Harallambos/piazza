# RESOURCES SERVER SERIALIZERS FILE
# ------------------------------------------------------------------------------------------------------------------------
from rest_framework import serializers
from .models import Post, Comment, Topic
from django.contrib.auth.models import User



# Comment Serializer
# ------------------------------------------------------------------------------------------------------------------------
class CommentSerializer(serializers.ModelSerializer):

	current_user = serializers.SerializerMethodField('get_username')
	current_user_id = serializers.SerializerMethodField('get_user_id')


	# Use this method for the custom field
	def get_user_id(self, obj):
		request = self.context.get('request', None)
		if request:
			return request.user.id
	
	# Use this method for the custom field current_user
	def get_username(self, obj):
		request = self.context.get('request', None)
		if request:
			return request.user.username

	class Meta:
		model = Comment
		fields = ('post', 'content', 'current_user_id', 'current_user')


# Post Serializer
# ------------------------------------------------------------------------------------------------------------------------
class PostSerializer(serializers.ModelSerializer):

	# calling the post_status function from our post model and store it in the  status_of_post variable which will add to our 
	# post serializer fields. 
	status_of_post = serializers.ReadOnlyField(source='post_status')
	current_user = serializers.SerializerMethodField('get_username')
	number_of_likes = serializers.ReadOnlyField(source='total_likes')
	current_user_id = serializers.SerializerMethodField('get_user_id')

	# Use this method for the custom field
	def get_user_id(self, obj):
		request = self.context.get('request', None)
		if request:
			return request.user.id
	
	# Use this method for the custom field
	def get_username(self, obj):
		request = self.context.get('request', None)
		if request:
			return request.user.username
		
	class Meta:
		model = Post
		fields = ('title', 'topic', 'content', 'expiration_date', 'author', 'status_of_post', 'current_user_id', 'current_user', 'number_of_likes')
		
		


# Topic Serializer
# ------------------------------------------------------------------------------------------------------------------------
class TopicSerializer(serializers.ModelSerializer):
	
	
	class Meta:
		model = Topic
		fields = ('name', )


