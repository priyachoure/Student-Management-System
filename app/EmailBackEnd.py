from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailBackEnd(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        usermodel = get_user_model()
        try:
            user = usermodel.objects.get(email=username)
        except usermodel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None


"""
The code you've provided is a Python class called EmailBackEnd that seems to be intended for use in Django for 
authentication purposes. This class appears to be a custom authentication backend, which is a way to customize
 how users can be authenticated in a Django application. The purpose of this specific backend is to allow users 
 to log in using their email addresses as opposed to the default username.

Here's an explanation of what the code does:

class EmailBackEnd(ModelBackend)::

This class is defined and inherits from ModelBackend, which is part of Django's authentication system.
def authenticate(self, username=None, password=None, **kwargs)::

This method is part of the authentication backend. It is called when a user tries to log in.
usermodel = get_user_model():

This line retrieves the user model for the Django project. It's a way to get the user model dynamically,
 allowing for flexibility.
 
Inside a try...except block:

user = usermodel.objects.get(email=username):
This line attempts to find a user in the database whose email matches the provided username. 
If a user with that email is found, it's stored in the user variable.

except usermodel.DoesNotExist::
If no user is found with the given email, this exception is raised. In this case, None is returned, 
indicating that no user with the provided email exists.
else::

If the try block does not raise an exception (meaning a user with the provided email exists), it checks the 
user's password.
if user.check_password(password)::

This line checks whether the provided password matches the user's stored password. If they match, it means the user has
 entered the correct password.
If the password matches, return user is called, and the user is considered authenticated and logged in.

If the password doesn't match or the user doesn't exist with the provided email, the method returns None,
 indicating that the login attempt was unsuccessful.

This code is a common approach for implementing email-based authentication in Django, allowing users to log 
in with their email addresses instead of usernames. It's often used when you want to customize the default 
authentication behavior provided by Django
"""
