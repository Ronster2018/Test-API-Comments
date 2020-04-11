from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from datetime import datetime
from django.urls import reverse


# Create your models here.

class Test(models.Model):  # Food = Nodes on Link
    owner = models.ForeignKey('auth.User',
                              null=False,
                              blank=True,
                              # i.e the link objects
                              on_delete=models.CASCADE) # if the item is deleted, then the Link to it are deleted
    # adjacent = {}
    id = models.AutoField(primary_key=True)  # auto incrimented PK
    title = models.CharField(max_length=75, unique=True)
    comment_text = models.TextField(max_length=120, null=True, blank=True)
    date_added = models.DateTimeField("Date added", default=datetime.now())
    allow_comments = models.BooleanField('allow comments', default=True)
   

    def __str__(self):
        return self.title
