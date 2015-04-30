from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Activity(models.Model):
    ACTIVITY_TYPE = (
        ('p', 'Photo'),
        ('l', 'Like'),
        ('c', 'Comment'),
    )
    user_id = models.ForeignKey(User)
    timestamp = models.DateTimeField()
    activity_type = models.CharField(max_length=30,choices=ACTIVITY_TYPE)
    data = models.CharField(max_length=300)

class Photo(models.Model):
    image_url = models.CharField(max_length=300)
    commentCount = models.IntegerField()
    likeCount = models.IntegerField()
