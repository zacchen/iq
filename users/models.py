from django.db import models
from users.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    """
    !!! To use this guy we need to put:
        AUTH_PROFILE_MODULE = 'users.User'    
    !!! in our settings.py

    Above is the (current) preferred method for extending the Django user 
    Base model. AbstractUser is effectively the Django User model.
    
    We let the Django user model provide the following attributes:
        username, first_name, last_name, email, password, groups, 
        user_permissions, is_staff, is_active, is_superuser, last_login, 
        date_joined
    And the following methods:
        is_anonymous(), is_authenticated(), get_full_name(), 
        set_password(raw_password), check_password(raw_password), 
        set_unusable_password(), has_usable_password(), 
        get_group_permissions(obj=None), get_all_permissions(obj=None), 
        has_module_perms(package_name), get_profile()
    """ 
    title =             models.CharField(max_lengh=50)
    avatar =            models.ImageField()
    phone =             models.intergerField()
    mailing =           models.BooleanField()
    dob =               models.DateField()
    country =           models.CharField(max_lengh = 255)
    password_hint =     models.charField(max_lengh = 255)
    password_hint_response = models.charField(max_lengh = 255)
    user_occupation =   models.charField(max_lengh = 255)
    signoff =           models.CharField(max_lengh = 255)
    
    class Meta():
        ordering = ('date_joined',)
        get_latest_by = ('last_login',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'


    USERNAME_FIELD = 'email'


#class Activation
#    user =              models.ForeignKey(User)
#    activation_key =    models.CharField(max_lengh = 255)
#    activation_sent =   models.BooleanField()
#    activation_returned = models.BooleanField()
#    
#class State(models.Model)
#    name =              models.CharField()
#    can_login =         models.BooleanField()
#
