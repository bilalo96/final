from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


# Create your models here.

class About(models.Model):
    what_we_do = models.TextField(max_length=1000)
    our_mission = models.TextField(max_length=1000)
    our_goal = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='about/')
    why_choose_us =  models.TextField(max_length=1000)

    class Meta:
        verbose_name = ("About")
        verbose_name_plural = ("About")

    def __str__(self):
        return str(self.id)

    # def get_absolute_url(self):
    #     return reverse("About_detail", kwargs={"pk": self.pk})



class FAQ(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)


    class Meta:
        verbose_name = ("FAQ")
        verbose_name_plural = ("FAQ")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("FAQ_detail", kwargs={"pk": self.pk})


class Info(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to="company/")
    description = models.TextField(max_length=500)
    fb_url = models.URLField(max_length=200 , blank=True, null=True)
    twitter_url = models.URLField(max_length=200 , blank=True, null=True)
    Instgram_url = models.URLField(max_length=200 , blank=True, null=True)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    mail = models.EmailField( max_length=254)



    class Meta:
        verbose_name = ("Info")
        verbose_name_plural = ("Info")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Info_detail", kwargs={"pk": self.pk})


class NewsLetter(models.Model):
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(default=timezone.now())


    class Meta:
        verbose_name = ("newsletter")
        verbose_name_plural = ("newsletters")

    def __str__(self):
        return self.email


class Testimonial(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    position = models.CharField(max_length=255, verbose_name=_("Position"))
    country = models.CharField(max_length=255, verbose_name=_("Country"), blank=True, null=True)
    message = models.TextField(verbose_name=_("Message"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active"))

    def __str__(self):
        return self.name
