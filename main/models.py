from django.db import models
from django.contrib.auth.models import User,AbstractUser
from .manager import CustomeUserManger
from django.utils.translation import gettext_lazy  as _
# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField('emial address' , unique=True)
    name= models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=12)
    date_of_birth = models.DateField(null=True,)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomeUserManger()

    def __str__(self):
        return self.email



class Apps(models.Model):
    img = models.ImageField(upload_to='icon')
    app_name = models.CharField(max_length=100)
    app_link = models.CharField(max_length=1000)
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    point = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

status = (
    ('complate','complate'),
    ('not complate','not complate')
)
class Points(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    x = models.ForeignKey(Apps, on_delete=models.CASCADE)
    success_img = models.ImageField(upload_to = 'success-img')
    status = models.CharField(max_length=15,choices=status,default="not complate")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)