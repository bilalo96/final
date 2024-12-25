from django.shortcuts import render
import requests
from car.models import Car,Category
from django.db.models.query_utils import Q
from django.db.models import Count
from blog.models import Post
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .models import FAQ , About , Info , NewsLetter
from django.conf import settings
from django.views.generic import ListView
from .tasks import send_mail_task
from blog import models as blog_models
from car import models as car_models
from django.http import JsonResponse
from django.core.paginator import Paginator


# Create your views here.


import requests
from django.shortcuts import render

API_KEY = "AIzaSyConLaaE3huRz1-ADfsNAJmwVHyJc0-YP8"
PLACE_ID = "ChIJ0zWPCohpXz4RYviYaLsn_30"

def fetch_reviews():
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={PLACE_ID}&fields=reviews&key={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        reviews = data.get("result", {}).get("reviews", [])
        return reviews
    except requests.exceptions.RequestException as e:
        print(f"Error fetching reviews: {e}")
        return []

def reviews_view(request):
    reviews = fetch_reviews()  # استدعاء الدالة التي تجلب التقييمات
    paginator = Paginator(reviews, 5)  # 5 تقييمات لكل صفحة
    page_number = request.GET.get('page')  # الحصول على رقم الصفحة من الـ GET parameter
    page_obj = paginator.get_page(page_number)

    reviews_data = [{
        'author_name': review['author_name'],
        'rating': review['rating'],
        'text': review['text']
    } for review in page_obj]

    return JsonResponse({'reviews': reviews_data, 'has_next': page_obj.has_next()})



def home(request):
    category=Category.objects.all()
    Sedan_list=Car.objects.filter(category__name='Sedan')[:5]
    Sport_list=Car.objects.filter(category__name='Sport')[:4]
    Economy_list=Car.objects.filter(category__name='Economy')[:4]
    Suv_list=Car.objects.filter(category__name='Suv')[:4]
    Starter_list=Car.objects.filter(starter=1)
    recent_posts=Post.objects.all()[:4]
    users_count=User.objects.all().count()
    #places_count=Car.objects.filter(category__name='Places').count()
    Economy_count=Car.objects.filter(category__name='Economy').count()
    Sedan_count=Car.objects.filter(category__name='Sedan').count()
    Sport_count=Car.objects.filter(category__name='Sport').count()
    Suv_count=Car.objects.filter(category__name='Suv').count()
    Starter_count=Car.objects.filter(starter=1).count()
    reviews = fetch_reviews()



    return render(request,'settings/home.html',{
        #'places': places ,
        'category': category,
        'Sedan_list':Sedan_list,
        'Sport_list':Sport_list,
        'Suv_list':Suv_list,
        'Economy_list':Economy_list,
        'Starter_list':Starter_list,
        'recent_posts':recent_posts,
        'users_count':users_count,
        #'places_count':places_count,
        'Sedan_count':Sedan_count,
        'Sport_count':Sport_count,
        'Economy_count':Economy_count,
        'Suv_count':Suv_count,
        'Starter_count':Starter_count,
        'reviews': reviews,
    })


def home_search(request):
    name=request.GET.get('name')
    category=request.GET.get('category','')
    car_list=Car.objects.filter(
        Q(name__icontains= name)
            )
    return render(request,'settings/home_search.html',{'car_list':car_list})


def category_filter(request,category):
    category=Category.objects.get(name=category)
    car_list=Car.objects.filter(category=category)
    return render(request,'settings/home_search.html',{'car_list':car_list})

class AboutView(ListView):
    model = FAQ
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.last()
        return context





def contact(request):
    site_info = Info.objects.last()

    if request.method == 'POST':
        subject= request.POST['subject']
        name= request.POST['name']
        email= request.POST['email']
        message= request.POST['message']

        send_mail_task.delay(subject,
        f'message from{name}\n email:{email} \n Message:{message}',
        email,
        [settings.EMAIL_HOST_USER],
        )

    return render(request,'settings/contact.html',{'site_info': site_info})


def dashboard(request):
    posts = blog_models.Post.objects.all().count()
    sport_count = car_models.Car.objects.filter(category__name='Sport').count()
    suv_count = car_models.Car.objects.filter(category__name='Suv').count()
    economy_count = car_models.Car.objects.filter(category__name='Economy').count()
    sedan_count = car_models.Car.objects.filter(category__name='Sedan').count()



    return render(request,'settings/dashboard.html',{

        'post_count' :posts,
        'sport_count':sport_count,
        'suv_count':suv_count,
        'economy_count':economy_count,
        'sedan_count':sedan_count,
    })

def news_letter_subscribe(request):
    email = request.POST.get('emailInput')
    NewsLetter.objects.create(email=email)
    return JsonResponse({'done':'done '})
























