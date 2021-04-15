CONTENTS

ABSTRACT……………………………………………………….…………………………………………….……..………………..................................................................3
INTRODUCTION……………………………………………………............................................................................................4
PREPARATION PHASE: INSTALL AND CONFIGURE DJANGO AND DEPLOY SOFTWARE IN VIRTUALISED ENVIRONMENTS )….……………………………………………………………..7
PHASE 1: DEVELOPMENT OF AUTHORISATION AND AUTHENTICATION SERVICES (PIAZZA_API)……………………………………………………………………….….….……….……………………….8
PHASE 2: DEVELOPMENT OF PIAZZA RESTFUL API (AUTH_SERVER)………………………..….……...................................................…12
PHASE 3: DEVELOPMENT OF RESOUCE APPLICATION (RESOURCE_SERVER) (AUTH_SERVER)….…………………………………………………………………………………………………….……....…20
PHASE 4: DEVELOPMENT OF APPLICATION BROWSER…………………………………..………………….........................................................…30
TEST CASES……………………………….…………….…………………………………………………………………….................................................................….…31
CODE…………………………..……………………….………………………………………………….…………………...................................................................………53
AUTH_SERVER CODE……………………………..………………………………………………………………..………................................................................…58
RESOURCES_SERVER CODE……………………………….………………………………………………………….…................................................................…20
PIAZZA_APICODE……………………………..……………………………………………………………...……..…………..............................................................58








ABSTRACT

In this coursework we have developed a RESTful SaaS for a system system called Piazza using the Django RESTful API framework. In Piazza, users post messages for a particular topic while other users browse posts per topic and perform basic interactions, including like and add a comment. We are using the OAuth 2.0 protocol which is the industry-standard for authorization. 
This application was developed in main 4 phases:
Preprocess Phase : Installing and configuring Django
Phase 1: Development of an authorization server (PIAZZA_API)
Phase 2: Development of an application server (AUTH_SERVER)
Phase 3: Development of a resources server (RESOURCES_SERVER)
Phase 4: Application browser (Jupyter Notbook - PIAZZA API TESTER APPLICATION.ipynb )


Piazza supports the following actions. 

Action 1: Authorised users access the Piazza API using the oAuth v2 protocol. 
Action 2: Authorised users post a message for a particular topic in the Piazza API. 
Action 3: Registered users browse messages per topic using the Piazza API. 
Action 4: Registered users perform basic operations, including “like”, “comment” a message posted for a topic. 
Action 5: Authorised users could browse for the most active post per topic that has the highest total number of likes. 
Action 6: Authorised users could browse the history data of expired posts per topic 







INTRODUCTION 

[2] OAuth 2.0 is the industry-standard protocol for authorization. It is an authorization framework which gives applications limited access to user accounts on an HTTP service such as Piazza. The OAuth 2.0 authorization framework enables a third-party application to obtain limited access to an HTTP service, either on behalf of a resource owner by orchestrating an approval interaction between the resource owner and the HTTP service, or by allowing the third-party application to obtain access on its own behalf.  This specification replaces and obsoletes the OAuth 1.0 protocol described in RFC 5849. In this coursework we will setup the OAuth v2 in Django, then we will create a simple application to authorize our users to access resources (our data). 

These are the development phases of our application.

         PHASE 4                    PHASE 2                   PHASE 1                      PHASE 3
 

Preprocess Phase : Installing and configuring Django

Phase 1: Development of an authorization server (PIAZZA_API)
•Django REST and oAuth protocol to develop a server to manage authentication. 

Phase 2: Development of an application server (AUTH_SERVER)
• Creating a (AUTH_SERVER) application as an application server, the server will connect to the authorization server and create users and tokens for authentication. 

Phase 3: Development of a resource server (RESOURCES_SERVER)
• Creating a “movies” application (as a resources server) as an API for storing and manipulating data for movies. 

Phase 4: Application browser (Jupyter Notbook - PIAZZA API TESTER APPLICATION.ipynb )
• A python script to remotely interact with the application server to authorize users to access the movies (resources server). 
• This is our testing application to test the functionality of our servers.
After creating our application server (AUTH_SERVER) in Phase 2 we are now able to see in the Django admin page that we have the DJANGO OAUTH TOOLKIT. We can now go and register our application with the service. This can be done from the Django admin panel: http://10.61.64.32:8000/admin/  
 
or it can be registered at the following url: http://10.61.64.32:8000/o/applications/


When the application is finaly registered, we receive: Client ID and Client Secret which are given from our AUTH_SERVER. We need to add them to the views.py file of our resource server application RESOURCES_SERVER that we will develop in Phase 3. 
CLIENT_ID = '8RPubhMrs7GZHVrFe4AvcTAXAvCFOJFyvwHKhZQH'
CLIENT_SECRET = '2coWq1bb0cnP4zviaH4E7aKQNJXicKetQUaoaYNsivNODeesP80PughOWU86phlv35gZAx843fd3nOp9rDld5MAYdKfGrW83AZKGNKD472lU6CAzSgGJVKonFNvFnQwB'



Now that we have our PIAZZA application registered, we can use the Oauth2 API endpoints: 
•	register users: http://10.61.64.32:8000/auth/register/ 
•	get a token: http://10.61.64.32:8000/auth/token/ 
•	refresh a token: http://10.61.64.32:8000/auth/token/refresh/
•	revoke a token: http://10.61.64.32:8000/auth/token/revoke/ 
In the next phase we developed our resources application which we called RESOURCES_SERVER. We have developed a WEB application where users can register login and create posts and topics for the posts , search by topic and add comment and like to posts of other users. The PIAZZA website portal is: http://10.61.64.32:8000/
 
In the final phase we will go through some test-cases to test our application’s functionality. For this phase a Jupiter notbook is used to run the test cases and do post calls to our API endpoints. Which will be described in detail in this report.








PREPARATION PHASE: INSTALL AND CONFIGURE DJANGO AND DEPLOY SOFTWARE IN VIRTUALISED ENVIRONMENTS 
The virtual machine IP that has been used to develop this project is: 10.61.64.32
We have created a new virtual environment folder for developing our application which is called PIAZZA-API 
/home/student/PIAZZA-API
 
After activating our PIAZZA-API environment we have installed:
•	Django 3.0.2 
•	django-rest-framework
•	django-oauth-toolkit

We created then our first application PIAZZA_API and copied it inside a folder called src (wich will be our project source folder)
/home/student/PIAZZA-API/src
 
Then we created our Django project called PIAZZA_API
In this PIAZZA_API Django project we will develop our authorization server, resources server and application server. 
 
We added our VM’s IP address in the the settings.py file on the ALLOWED_HOSTS = ['10.61.64.32']
PHASE 1: DEVELOPMENT OF AUTHORISATION AND AUTHENTICATION SERVICES (PIAZZA_API)
In this phase we are going to develop our authorisation server.
 
We have added in our settings.py file the code marked with red boxes in the following picture.
INSTALLED_APPS: This is where Django discovers your apps.
MIDDLEWARE: Each time a request is coming into Django server the middleware hooks into Django’s request/response processing.
REST_FRAMEWORK: These are the settings for Django REST to accept OAuth2 as authentication middleware.
AUTHENTICATION_BACKENDS: This specifies what authentication system should be used.

 
Next step is to add your OAuth2 provider. For this step we need to edis our urls.py file and add the path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')) to our urlpatterns. This way we create a new URL in the form http://IP:8000/o where o is the resources for performing the authentication phase (“o” for “oAuth”). 

 


Then we run migrations to create db.sqlite3 databse and make tables for our models. We need to create a Django superuser in oreder to be able to login to the Django admin page: http://10.61.64.32:8000/admin and manage our application resources. 
Django superuser credentials:
username: admin
password: xd!4563izi

 

Sumarry of the phase B: 
•	We have deplayed and configured our authorisation server.
•	Each time an application (Application browser) requires access to a resources (Resources server), it will need to have the appropriate security credentials. 
•	This means that each application will need to register and request for an access token to access our resources e.g., an API. 
•	The token will be used each time the application sends a request to the application server to retrieve data. 
•	The token is nothing else than a long string that is unique for every user. 
Let’s check now the API endpoints:

User registration : http://10.61.64.32:8000/auth/register/ 
Register user to the server and receive  access tokens with username and password. Input should be in the format:
{"username": "username", "password": "1234abcd"}
 

Get a token: http://10.61.64.32:8000/auth/token/ 
Get tokens with username and password. Input should be in the format:
{"username": "username", "password": "1234abcd"}
 

Refresh token: http://10.61.64.32:8000/auth/token/refresh/ 

Refresh a token providing a non expired token. Input should be in the format:

{"refresh_token": "<token>"}

 


revoke token: http://10.61.64.32:8000/auth/token/revoke/ 

Method to revoke tokens
.
{"token": "<token>"}

 


PHASE 2: DEVELOPMENT OF PIAZZA RESTFUL API (AUTH_SERVER)

 

So far, we have created our authentication server. 
The next step is to create a new application for users to authorize and register directly using the authorization server. We will call this application AUTH_SERVER and it will be our applications server. To use it, we will design a simple RESTFul API 


 





We create the application and add the application in settings.py file at INSTALLED_APPS. 

 

We create a serializers.py file to serialize our models. 

 


Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.
The serializers in REST framework work very similarly to Django's Form and ModelForm classes. We provide a Serializer class which gives you a powerful, generic way to control the output of your responses, as well as a ModelSerializer class which provides a useful shortcut for creating serializers that deal with model instances and querysets. 
The create method overrides the default class when saving data for a user, this is important to make sure the password is hashed correctly. The metadata include the details of a user, that is each has an id a username and a password. Next step is to register an application. 
There are 2 ways to do this: Via the Django admin panel. 

1st WAY
Firstly, click on Applications. 

 

Click ADD APPLICATION

 


Find your application (or the django admin user if you have not already registered an application ) and click on your name using the lookup option (magnifier) and then copy this cliend id and client secret to a text editor so we can use them in the views.py file

 


















2nd WAY
Go to http://10.61.64.32:8000/o/applications/ and there you can register a new application. Click add new application
 
Then add all the details and the name for the new application and click save.
 
We have already done this for PIAZZA
 

CLIENT_ID = '8RPubhMrs7GZHVrFe4AvcTAXAvCFOJFyvwHKhZQH'
CLIENT_SECRET = '2coWq1bb0cnP4zviaH4E7aKQNJXicKetQUaoaYNsivNODeesP80PughOWU86phlv35gZAx843fd3nOp9rDld5MAYdKfGrW83AZKGNKD472lU6CAzSgGJVKonFNvFnQwB'

Next step is to create our API views.py  file. We copy and paste the code from file: 
	https://www.dropbox.com/s/qe7ie1rk98sp8vc/views.py?dl=0 
as shown in the lab 4.
We only change these parts in the code:
 
After the views.py file we must create our urls.py file for the AUTH_SERVER application.
 
Now we go to our PIAZZA_API/urls.py file and add this path to the uslpatterns 
path('authentication/', include('users.urls')),
 

We can now go and visit our API registration url: http://10.61.64.32:8000/auth/register/ 
 

We now need to make a post request in a JSON format : 
{"username": "username", "password": "1234abcd"}
After the registration we will receive a response 

 

{ 
"access_token": "6CCfLXQsX8CvuEnMvSH8NpQXdUvsMa", 
"expires_in": 36000, 
"token_type": "Bearer", 
"scope": "read write", 
"refresh_token": "ErJKt0W3iqzQ0mSBKCeXtmDl717QlU" 
}
By now we created an authorization server and a “AUTH_SERVER” application (application server). The “AUTH_SERVER” application is a simple user management system to create users using the API. This will allow us to create users remotely, get a user token and use it to access resources 
We  will create our website application now and we will call it:  RESOURCES_SERVER and this is also our PIAZZA WEB application.
 
This will also be our resources server where all the posts, comments and topics and user profiles will be stored. Please see in the CODE paragraph for the code details.












PHASE 3: DEVELOPMENT OF THE RESOURCES APPLICATION (RESOURCES_SERVER)               
First let’s explore our front-end website interface and the endpoints. 
PIAZZA MAIN PAGE: http://10.61.64.32:8000/
  
In this view we can see a list of all the posts created by users with the latest one appearing on the top of the list. So the posts are sorted my most recent date. If we click on PIAZZA it takes us to the home page wich is this same view. On every post we can see the:

 

•	Post title
•	Post author
•	Date posted
•	Post content
•	Number of likes
•	Status (LIVE or EXPIRED)
If we click Topics: http://10.61.64.32:8000/topic_list/ 
 
This takes use to a list of topics that we can click and when we click a topic, we can then see all the posts that are posted on that topic again sorted by most recent date showing on top of the list. Let’ s see what is in the health topic: http://10.61.64.32:8000/topic/health    
 


Next option is the regiter button wich will take us to the new user registration form: http://10.61.64.32:8000/auth/registration/ 
 
Here we can register a new user to the PIAZZA WEB APP. When the user is registered it redirects the user to our login page: http://10.61.64.32:8000/auth/login/ 
 

We have already the Django admin user created so let’s login to see what ather options we have. 
 











We can now see the there are 3 more options available:
Add post: http://10.61.64.32:8000/add_post/ 
 
We can add a new post here by adding ,
•	Title
•	title tag (this wat will appear in our webpage tab)
•	Content
•	Status (LIVE OR EXPIRED)
•	Expiration date that you can edit manually
•	A dropdown menu of the available topics to choose from




Next option is Add topic:  http://10.61.64.32:8000/add_topic/ 
 
Here we can manually add a topic this is an extra option the has been implemented on the PIAZA application itially this was created by just having a selection list hardcoded on the Post model with a list of topics so if we wanted to add more topics we had to go manually and change the code but this way we can add mor  topics just by the PIAZZA web interface. For this to work we have crewated a moden for topic . 
Next available option when a user is loged in is the Edit profile: http://10.61.64.32:8000/auth/edit_profile/ 
 
This can be used to change account settings. There is even a password change link which prompts the users to a page to change their password: by clicking on the : 

 

Cahange password form: http://10.61.64.32:8000/auth/password/ 
 
The next option is the Logout option, and this will log the user out from the PIAZZA WEB SITE. The is one more record in the navbar but this is just displaying the current loggedin user’s username. In our case says admin as we are logged in with the admin account.
















Let’s see now the API url’s of our RESOURCES_SERVER.

Post model API view: http://10.61.64.32:8000/api/post/
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
 








Comment model API view: http://10.61.64.32:8000/api/comment/ 
Adds a comment on a post. Input should be in the format:

{
"post": "title",

"content":"content",

}

API URL: http://10.61.64.32:8000/api/comment/
 







Topic model API view: http://10.61.64.32:8000/api/topic/
{
"name":"name",
}

API URL: http://10.61.64.32:8000/api/topic/
 


PHASE 4: DEVELOPMENT OF APPLICATION BROWSER               (Jupyter Notbook - PIAZZA API TESTER APPLICATION.ipynb)

For our testcases we used a Jupyter notebook (PIAZZA API TESTER APPLICATION.ipynb) as we did in the labs to perform calls to the authentication API endpoints and grant users access with returning an access token that expires in a certain amount of time that can be edited in the PIAZZA_API/settings.py file the last line of code at the end of the file.
# Set the time for a token to expire in 10 hours = 10 * 60 minutes = 10 * 60 * 60 secondes (36000 sec) 
# BY CHANGING THAT VALUE WE CAN DECITE HOW LONG AN ACCESS TOKEN IS VALID FOR.
OAUTH2_PROVIDER = {
        'ACCESS_TOKEN_EXPIRE_SECONDS': 36000,
 }

IMPORTANT
Before we start the tast cases we can go login to PIAZZA http://10.61.64.32:8000/auth/login/ with the Django admin user 
(username: admin, password: xd!4563izi) 
and create the topics that are given in the coursework description (tech, sports, politics, health). Go to http://10.61.64.32:8000/add_topic/ and add the topics. 
 

TEST CASES
Let us assume a use case scenario of four users such as Olga, Nick, Mary, and Nestor that access the Piazza API. Provide the following test cases (TCs).

TEST CASE 1
Olga, Nick, Mary, and Nestor register and are ready to access the Piazza API. 
________________________________________
We can register users with 3 diferent ways.
1. With a POST request to our API endpoind for user registration: http://10.61.64.32:8000/auth/register 
2. Via the PIAZZA website register link: http://10.61.64.32:8000/auth/registration/ 
3. From the admin panel with adding a new user: http://10.61.64.32:8000/admin/auth/user/add/ 
Will do all 3 of them with different users to demonstrate that all 3 methods are working
1.	With a POST request to our API endpoind for user registration
 
RESPONSE:
{'access_token': 'M9lZuLnePh50cRk9ZKUQG5DRSquaAG', 'expires_in': 36000, 'token_type': 'Bearer', 'scope': 'read write', 'refresh_token': 'I6yA8zcLcPpST52Maec76tdzpv1fZJ'}

2. Via the PIAZZA website register link: http://10.61.64.32:8000/auth/registration/  user Nick

 

3.	From the admin panel with adding a new user Mary: http://10.61.64.32:8000/admin/auth/user/add/
 
4.	With a POST request to our API endpoind for user registration for user Nestor:
 

RESPONSE:
{'access_token': 'bnew8ICvRVPKP3AFCzLPDZgYt3FfxO', 'expires_in': 36000, 'token_type': 'Bearer', 'scope': 'read write', 'refresh_token': 'Wxa8VWViPgU959AJVT3QfNEQNMPQzQ'}

We have now registered our 4 users 
 


But if we see in the Access tokentsa page we can see that only 2 tokens were given to users and this is because only users Nestor and Olga were registered by the call to the PIAZZA API hence only these users received tokens.
 Let’s try now in Test Case 2 to get tokens for the other 2 users with a call to the http://10.61.64.32:8000/auth/token/ API endpoint

TEST CASE 2
Olga, Nick, Mary, and Nestor use the oAuth v2 authorisation service to register and get their tokens. 
________________________________________

Nestor: 
token: bnew8ICvRVPKP3AFCzLPDZgYt3FfxO  
exp date:  April 13, 2021, 8:27 a.m.

Olga: 
Token: M9lZuLnePh50cRk9ZKUQG5DRSquaAG 
Exp date:  April 13, 2021, 8:24 a.m.









We need to get a token for Mary and one for Nick.
We will request a token with a post html call at the http://10.61.64.32:8000/auth/token/ API endpoint with our jupyter notbook script
 
RESPONSE: 
token: HjzlvsFRJQctPMQtHigMyw0GvMiV0f 
token expiration time in seconds: 36000

Mary: 
Token: HjzlvsFRJQctPMQtHigMyw0GvMiV0f
Exp date:  April 13, 2021, 8:43 a.m.




 

RESPONSE: 
token: 6Ab0gli8ao7QOFFnXAhASNKoQvfAlp 
token expiration time in seconds: 36000

Nick: 
Token: 6Ab0gli8ao7QOFFnXAhASNKoQvfAlp
Exp date:  April 13, 2021, 8:48 a.m.





We have all 4 users now with their access tokens that expire in 36000 seconds (10 hours)
Nestor: 
token: bnew8ICvRVPKP3AFCzLPDZgYt3FfxO  
exp date:  April 13, 2021, 8:27 a.m.
Olga: 
Token: M9lZuLnePh50cRk9ZKUQG5DRSquaAG 
Exp date:  April 13, 2021, 8:24 a.m.
Mary: 
Token: HjzlvsFRJQctPMQtHigMyw0GvMiV0f
Exp date:  April 13, 2021, 8:43 a.m.
Nick: 
Token: 6Ab0gli8ao7QOFFnXAhASNKoQvfAlp
Exp date:  April 13, 2021, 8:48 a.m.














TEST CASE 3
Olga makes a call to the API without using her token. This call should be unsuccessful as the user is unauthorised. 
________________________________________

Olga no has an access token but let’s make a request with a not valid access token just to test that the application is protected.
 
RESPONSE:
{'detail': 'Authentication credentials were not provided.'}

Great this means that our API is protected.


TEST CASE 4
Olga posts a message in the Tech topic with an expiration time (e.g. 5 minutes) using her token. After the end of the expiration time, the message will not accept any further user interactions (likes, dislikes, or comments). 

________________________________________
We run a POST call to our post API endpoint: http://10.61.64.32:8000/api/post/ 
 
RESPONSE:
{'title': "Olga's 1st post from the API", 'topic': 'tech', 'content': 'This is Olgas 1st post created by the API', 'expiration_date': '2021-04-13T12:11:00Z', 'author': 8, 'status_of_post': 'LIVE', 'current_user_id': 8, 'current_user': 'Olga', 'number_of_likes': 0}

This is Olgas 1st  Post using the API with her access token.

TEST CASE 5
Nick posts a message in the Tech topic with an expiration time using his token. 

________________________________________
 
RESPONSE:
{'title': "Nicks's 1st post from the API", 'topic': 'tech', 'content': "This is Nick's 1st post created by the API", 'expiration_date': '2021-04-13T12:30:00Z', 'author': 11, 'status_of_post': 'LIVE', 'current_user_id': 11, 'current_user': 'Nick', 'number_of_likes': 0}





TEST CASE 6
Mary posts a message in the Tech topic with an expiration time using her token. 
________________________________________
 
RESPONSE:
{"title": "Marys's 1st post from the API", "topic": "tech", "content": "This is Marys 1st post created by the API", "expiration_date": "2021-04-13T12:30:00Z", "author": 10, "status_of_post": "LIVE", "current_user_id": 10, "current_user": "Mary", "number_of_likes": 0
}






TEST CASE 7
Nick and Olga browse all the available posts in the Tech topic, there should be three posts available with zero likes, zero dislikes and without any comments. 
________________________________________
To perform this test, we can login to our Piazza Website: http://10.61.64.32:8000/ 
Login first as Nick:
 
We can se that there are 3 posts and without any comments.
-	Here we need to mention that there is no dislike function developed for our site we have only a like function that can be unliked by the same user. 
-	Also, to see the comments we need to go and click on the post and then we should see the list of comments on the post. (need to put the number of comments to show in the main page with the list of comment on each comment individualy)

Login first as Olga:
 

TEST CASE 8
Nick and Olga “like” Mary’s post in the Tech topic. 
________________________________________
We login as olga click Marys Post and click like 
 
We then logout and login as Nick and like Mary’s Post.

 
We can see that there are 2 likes on Marys post now one from Nick and one from Olga.




TEST CASE 9
Nestor “likes” Nick’s post, and “dislikes” Mary’s post in the Tech topic. 
________________________________________
Login as Nestor and like nick’s post. 
 
There is no dislike function yet so we cannot perform the second action to dislike Mary’s post.
TEST CASE 10
Nick browses all the available posts in the Tech topic; at this stage he can see the number of likes and dislikes for each post (Mary has 2 likes and 1 dislike and Nick has 1 like). There are no comments made yet. 
________________________________________
We login as nick and browse the tech topic and we can see all the messages. 
We cannot see dislikes and we need to click in the post to see if there are any comments. 
(We should include a number of comments view on each post – to be implemented in next version as well as the dislike function)
 
( In the other hand we have implemented some other extra function such us the ability of updating a post but only for logged in users to be able to edit their post only or even delete their posts) 

TEST CASE 11
Mary likes her post in the Tech topic. This call should be unsuccessful, as in Piazza a post owner cannot like their own messages. 
________________________________________
We login as Mary click on Marys post and we will see that the like function is missin so Mary cannot like her post. We have implemented this by removing the like button on a post when the loggedin user id is the same with the post author id. 
 
She can still edit and delete her post or even add a comment on it.







TEST CASE 12
Nick and Olga comment for Mary’s post in the Tech topic in a round-robin fashion (one after the other adding at least 2 comments each). 
________________________________________
 
We can see all 4 comments , 2 from nick and 2 from Olga on Marys’s post.






TEST CASE 13
Nick browses all the available posts in the Tech topic; at this stage he can see the number of likes and dislikes of each post and the comments made. 
________________________________________
 
To be able to see the comments dates Nick must click on each comment
Let’s see the comments and their dates on Marys post
 

Comments and the dates are shown on the bottom of the post and are ordered by date. Lates posted comment is on the top of the list
TEST CASE 14
Nestor posts a message in the Health topic with an expiration time using her token. 
________________________________________
 
RESPONSE:
{ "title": "Nestor's 1st post from the API", "topic": "health", "content": "This is Nestor's 1st post created by the API", "expiration_date": "2021-04-13T01:50:00Z", "author": 9, "status_of_post": "LIVE", "current_user_id": 9, "current_user": "Nestor", "number_of_likes": 0 }







TEST CASE 15
Mary browses all the available posts in the Health topic; at this stage she can see only Nestor’s post. 
________________________________________
Login as mary and browse the health topic posts.
 

TEST CASE 16
Mary posts a comment in the Nestor’s message in the Health topic. 
________________________________________
 
TEST CASE 17
Mary dislikes Nestor’s message in the Health topic after the end of post expiration time. This should fail. 
________________________________________
-	Here we need to mention that the post from the API using the token even if we put an expiration date in the JASON format when we do the POST cal to the API the status of the post stays LIVE. 
-	If we create appost from within the PIAZZA website then the status goes to expired after the expiration time ends. Din’t really know or find a good way to implement the expiration date. We have just made a function on the post model that returns the status  LIVE or EXPIRED after checking the exp date with the date now. If date now is bigger then the status goes EXPIRED. 
-	But the functionality of removing the like and comment button when a post is expired still works is just the posts need to be made on the PIAZZA website and not with a call to the API.

 
We can see here after a test post we made the post went to expired status when the expiration date became smaller than the date now and if we click in that post we will see that we cannot add any comment or do alike action. 
 
Mary can still edit and delete the post as it is her own pos
TEST CASE 18
Nestor browses all the messages in the Health topic. There should be only post (his own) with one comment (Mary’s). 
________________________________________
 

 
It  is only one comment from mary on the Nestor’s post in the health topic which is the only post.



TEST CASE 19
Nick browses all the expired messages in the Sport topic. These should be empty. 
________________________________________
 

 
TEST CASE 20
Nestor queries for an active post having the highest interest (maximum sum of likes and dislikes) in the Tech topic. This should be Mary’s post. 

________________________________________
This function cannot be performed we have not implemented a way to check for the most popular post. We can amend the code and sort the post by the total number of likes and comments but is a feature we need to create in the next versio


CODE
The cod will be uploaded with the submition of the corsewrok but can also be found in the github repository: https://github.com/Harallambos/piazza.git 
 
The code is in the src folder: 
It contains: 
•	AUTH_SERVER -> Is our application for authorization
•	PIAZZA_API -> Is the main folder containingthe python files fro configuring our project.
•	RESOURCES_SERVER -> Is our application with all our resources, our resources server, containd all models, and html templates for our Piazza website.
 
AUTH_SERVER
 
PIAZZA_API
 









RESOURCES_SERVER
 
 

We used the Django default database db.sqlite3 and these are the tables we have created for our models.
 

























REFERENCES

SET UP DJANGO PROJECT – OAUTH2 ATHORISATION
[1]   Stelios Sotiriadis, Cloud Computing Module, Birkbeck University (classes and labs material)

HOW TO USE OAUTH2 FOR AUTHORISATION 
[2]   OAuth 2.0:  https://oauth.net/2/      
[3]   OAuth 2.0 Framework:  https://tools.ietf.org/html/rfc6749 
[4]   https://django.cowhite.com/blog/building-oauth2-services-in-django-with-django-oauth-toolkit/
[5]   https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2

DOCUMENTATION FOR DJANGO REST FRAMEWORK
[6]   Django Rest Framework: https://www.django-rest-framework.org/ 
[7]   Django project: https://www.djangoproject.com/ 

BUILDING THE PIAZZA WEBSITE (RESOURCES_SERVER)
[8]   John Elder from Codemy.com for Django tutorial for building a blog with Django https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&ab_channel=Codemy.com
[9]    LogRocket Blog: https://blog.logrocket.com/use-django-rest-framework-to-build-a-blog/
[10]   https://github.com/codingforentrepreneurs/Blog-API-with-Django-Rest-Framework 
[11]    
[12] 
[13]  
[14] 







