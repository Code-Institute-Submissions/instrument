<h1>Instrument</h1>
<img src="/static/readme_images/homepage.png">


<h3>Problem Statement</h3>
Instrument looks to simplify buying instruments for users. The usual websites for purchasing instruments are filled with a lot of distractions and a lot of accessories that distract from the instrument purchasing experience.


<h3>Proposed Solution</h3>
Instrument looks to simplify the purchasing of instruments by providing no distractions and just showcasing a select few instruments each month.


<h3>User Story 1: Signup, log-in, authentication and authorisation</h3>
<img src="/static/readme_images/signup.png">
A user is able to create an account. The user is able to log in with their own user credentials and is able to keep their account safe.

<h3>User Story 2: Viewing and searching for Products</h3>
<img src="/static/readme_images/basses.png">
The user is able to navigate to products using the dropdown menu and is able to search for specific products using the search bar.

<h3>User Story 3: Managing Products through the admin superuser</h3>
<img src="/static/readme_images/product_admin.png">
The user is able to create, delete, edit and generally manage products throught the admin superuser functionality that is available to them through the dropdown menu.


<h3>User Story 4: Keeping products in a shopping bag</h3>
<img src="/static/readme_images/add_to_bag.png">
<img src="/static/readme_images/shopping_bag.png">
The user is able to add products to the shopping bag and come back to them another time.

<h3>User Story 5: Purchasing products through the stripe integration</h3>
<img src="/static/readme_images/purchase.png">
A user is able to purchase a product through the stripe integration. 

<h3>User Story 6: A user receives email confirmations on purchases</h3> 

<h3>User Story 7: A user is able to see their own user profile page</h3> 
<h3>Current Bugs</h3>
<b>For some reason the profile.html template is not displaying as django says it is not there:</b>
<br>
TemplateDoesNotExist at /profile/
<br>
profiles/profile.html
<br>
Request Method:	GET
<br>
Request URL:	https://instrument-shop.herokuapp.com/profile/
<br>
Django Version:	3.1.5
<br>
Exception Type:	TemplateDoesNotExist
<br>
Exception Value:	
profiles/profile.html
<br>
Exception Location:	/app/.heroku/python/lib/python3.6/site-packages/django/template/loader.py, line 19, in get_template
<br>
Python Executable:	/app/.heroku/python/bin/python
<br>
Python Version:	3.6.12
<br>
Python Path:	
['/app/.heroku/python/bin',
 '/app',
 '/app/.heroku/python/lib/python36.zip',
 '/app/.heroku/python/lib/python3.6',
 '/app/.heroku/python/lib/python3.6/lib-dynload',
 '/app/.heroku/python/lib/python3.6/site-packages']
 <br>
Server time:	Mon, 01 Feb 2021 14:06:12 +0000

<h3>Technologies Used</h3>
Bootstrap

Google Fonts 

Python

[Django] https://docs.djangoproject.com/en/3.1/ for creating and managing applications, templates, views and urls.

CSS

[AWS] https://aws.amazon.com/ for storing the static files and the media files.

[Stripe] https://stripe.com/en-ie for handling payments.

<h3>Credits</h3>
- I mainly wanted to learn the concepts in this project so I followed the instructional videos as best as I could to recreate the system and code interactions from the instructional videos. I learned a lot from this and I am glad that I did as it consolidated a lot of the information and the concepts in my head.
<br>
- I wanted to also thank the CodeInstitute team for supporting me throughout the course especially in the end Lucy and her peers who were very kind to me in a difficult situation.
