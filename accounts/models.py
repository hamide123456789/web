from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from .usermanager import UserManager
# from.phone_field import phoneField

# error = {
#     'min_length':'حداقل باید 5 کاراکتر باشد',
#     'required':'این فیلد اجباری است',
#     'Invalid':'ایمیل شما نا معتبر است'
# }


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    # email = models.EmailField(unique=True ,error_messages= error)
    first_name = models.CharField(max_length=100)
    # first_name = models.CharField(max_length=10,min_length =5,error_messages=error)
    last_name = models.CharField(max_length=300)
    password = models.CharField(max_length=300)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    backend = 'accounts.backend.EmailBckend'

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=300)
    address = models.CharField(max_length=300,null=True,blank=True)

    def save_profile_user(sender, **kwargs):
        if kwargs['created']:
            profile_user = UserProfile(user=kwargs['instance'])
            profile_user.save()
    post_save.connect(save_profile_user, sender=User)

    def __str__(self):
        return self.user.email
    

