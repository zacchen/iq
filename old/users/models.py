from django.db import models
from users.models import User
# Create your models here.

class User(models.Model):
    title =             models.CharField(max_lengh=50)
    avatar =            models.ImageField()
    salt =              models.CharField(max_lengh=50)
    password =          models.CharField(max_lengh=50)
    email =             models.EmailField(max_lengh=255) 
    phone =             models.intergerField()
    mailing =           models.BooleanField()
    firstname =         models.CharField(max_lengh = 255)
    lastname =          models.CharField(max_lengh = 255)
    dob =               models.DateField()
    country =           models.CharField(max_lengh = 255)
    password_hint =     models.charField(max_lengh = 255)
    password_hint_response = models.charField(max_lengh = 255)
    user_occupation =   models.charField(max_lengh = 255)
    first_seen =        models.DateTimeField(auto_now_add = True)
    last_seen =         models.DateTimeField(auto_now = True)
#    user_group =            
    user_status =       models.ForeignKey(State)
    signoff =           models.CharField(max_lengh = 255)
    user_state =        models.ForeignKey(State)
    activated =         models.BooleanField()    
    class Meta():
        ordering = ('joined',)
        get_latest_by = ('last_seen',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'

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
