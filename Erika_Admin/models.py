from django.db import models

# Create your models here.

class Country(models.Model):
    city_name = models.CharField(max_length=100, default='kathmandu')


    def __str__(self):
        return self.city_name

class Profile_Images(models.Model):
    profile_Image = models.ImageField(upload_to='ProfileImg')

class Receive_Contact(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Messages = models.TextField()



    def __str__(self):
        return self.Name
    
class AboutMe(models.Model):
    Signature = models.CharField(max_length=50)
    Erika_Bio = models.TextField(max_length=200)
    Paragraph = models.TextField()
    Paragraph_1 = models.TextField(blank=True)
    Author_Image = models.ImageField(upload_to='Media', blank=True)

    def __str__(self):
        return self.Signature



class Books(models.Model):
    Books_Images = models.ImageField(upload_to='Media')
    Book_Link = models.CharField(max_length=200)
    Descriptions = models.TextField()

    def __str__(self):
        return self.Book_Link


class Reviews(models.Model):
    Reviews = models.TextField()

    def __str__(self):
        return self.Reviews