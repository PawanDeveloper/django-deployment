from django.db import models
from datetime import date
# Create your models here.
class User (models.Model):
    username = models.CharField('Username',max_length=100)
    firstname = models.CharField('Firstname',max_length=50)
    lastname = models.CharField('Lastname',max_length=50)
    email = models.EmailField('email',max_length=20)
    password = models.TextField('password',max_length=15)

# Blog create

class Blog(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    title = models.CharField('Post title',max_length=100)
    description = models.TextField('Post description')
    posted_date = models.DateField(default=date.today)
    good_name = models.CharField('Good name',max_length=100)

# comment create


class coment(models.Model):
    message = models.TextField('message')
    date_coment =  models.DateField(default=date.today)
    user_id =  models.ForeignKey(User,on_delete=models.CASCADE)
    post_id =  models.ForeignKey(Blog,on_delete=models.CASCADE)