import datetime
from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.
class Car(models.Model):
    owner=models.ForeignKey(User, related_name='car_owner', on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    image=models.ImageField( upload_to='car/')
    price=models.IntegerField(default=0)
    description=models.TextField(max_length=1000)
    category=models.ForeignKey('Category', related_name='car_category', on_delete=models.CASCADE)
    created_at=models.DateTimeField(default=datetime.datetime.now)
    slug=models.SlugField(null=True,blank=True)
    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug=slugify(self.name)

       super(Car, self).save(*args, **kwargs) # Call the real save() method


    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('car:car_detail', kwargs={'slug': self.slug})



    def check_avalibality(self):
        all_reservations=self.book_car.all()
        now=timezone.now().date()

        for reservation in all_reservations:
            if now > reservation.date_to:
                return 'Aviable'
            elif (now > reservation.date_from) & (now < reservation.date_to):
                reserved_to=reservation.date_to
                return f'Not Aviable {reserved_to}'

            else:
                return 'Aviable'

    def get_avg_rating(self):
      all_reviews=self.review_car.all()
      all_rating=0
      if len(all_reviews) > 0:
        for review in all_reviews:
            all_rating += review.rate
        return all_rating/len(all_reviews)
      else:
        return '-'


class CarImages(models.Model):
    car=models.ForeignKey('car',related_name='car_image',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='carimages/')
    def __str__(self):
        return str(self.car)


class Category(models.Model):
    name= models.CharField(max_length=50)
    icon= models.CharField(max_length=60)
    image = models.ImageField(upload_to='categoryimages/', default='default_image.jpg')
    def __str__(self):
        return self.name
class CarReview(models.Model):
    author = models.ForeignKey(User, related_name='review_author', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, related_name="review_car", on_delete=models.CASCADE)
    rate=models.IntegerField(default=0)
    feedback=models.TextField(max_length=500)
    created_at=models.DateTimeField(default=datetime.datetime.now)
    def __str__(self):
        return str(self.car)

COUNT=(
 (1,1),
 (2,2),
 (3,3),
 (4,4),
 (5,5)
)

class CarBook(models.Model):
   user = models.ForeignKey(User, related_name='book_owner', on_delete=models.CASCADE)
   car = models.ForeignKey(Car, related_name="book_car", on_delete=models.CASCADE)
   date_from=models.DateField(default=datetime.datetime.now)
   date_to=models.DateField(default=datetime.datetime.now)
   guest= models.IntegerField(choices=COUNT)
   children=models.IntegerField(choices=COUNT)
   slug=models.SlugField(null=True,blank=True)

   def __str__(self):
        return str(self.car)

   def  in_progress(self):
       now= timezone.now().date()
       return now > self.date_from and now < self.date_to
   in_progress.boolean=True








