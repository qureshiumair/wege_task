from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime



class UserInfoTable(AbstractUser):
    class Meta:
        app_label  = 'wege_backend'

    UserType = (("CUSTOMER","customer"),("STAFF","staff"),("SUPER_ADMIN","super-admin")) #ENUM for user_cateogry field
    username = models.CharField(max_length=30,null=False,unique=True)
    created_at = models.DateTimeField(default=datetime.now())
    user_category = models.CharField(max_length=20,null=False,choices=UserType,default="CUSTOMER")

    def __str__(self):
        return f"username:{self.username} email_id:{self.email}"