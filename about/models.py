from django.db import models

# Create your models here.
class About(models.Model):
    what_we_do=models.TextField(max_length=800)
    our_mission=models.TextField(max_length=800)
    our_goals=models.TextField(max_length=800)
    image=models.ImageField(upload_to='about/')


    def __str__(self):
        return str(self.id)


class FAQ(models.Model):
    title= models.CharField(max_length=50)
    description=models.TextField( max_length=50)


    def __str__(self):
        return self.title



