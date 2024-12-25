from django.urls import path
from .views import home,home_search ,category_filter , contact , dashboard ,news_letter_subscribe,reviews_view
from . import api_view

app_name='settings'


urlpatterns = [
    path('',home,name='home'),
    path('search',home_search,name='home_search'),
    path('newsletter',news_letter_subscribe,name='newsletter'),
    path('category/<slug:category>',category_filter,name='category_filter'),
    path('contact',contact,name='contact'),
    path('dashboard/',dashboard,name='dashboard'),
    path('about/api',api_view.about_api,name='about_api'),
    path('about/api/faq',api_view.faq_api,name='faq_api'),
    path('contact/api',api_view.contact_api,name='contact_api'),
    path('reviews/',reviews_view, name='reviews_view'),  # هنا يتم استدعاء الدالة الجديدة

]
