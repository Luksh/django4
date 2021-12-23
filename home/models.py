from django.db import models
from django.urls import reverse

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    subject = models.TextField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email} {self.subject} {self.message}"


class Feedback(models.Model):
    name = models.CharField(max_length=250)
    image = models.TextField()
    post = models.CharField(max_length=250)
    comment = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Information(models.Model):
    temp_address = models.TextField()
    per_address = models.TextField()
    phone = models.CharField(max_length= 500)
    timing = models.CharField(max_length=500)
    email = models.EmailField(max_length=250)

    def __str__(self):
        return f"{self.temp_address} "


class Blog(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    title = models.CharField(max_length=500)
    description = models.TextField()
    long_description = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'media')
    slug = models.TextField(blank=True)
    def __str__(self):
        return self.name

def get_blog_url(self):
    reverse('home:blog_details', kwargs={'slug':'self.slug'})