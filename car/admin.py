from django.contrib import admin
from .models import Car, CarBook, CarImages, CarReview, Category
from django_summernote.admin import SummernoteModelAdmin


class CarImagesInline(admin.TabularInline):
    model = CarImages
    extra = 1  # Set the number of image upload fields you want to display


class SomeModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    list_display = ('name', 'price_dialy','price_wek','price_monthly', 'get_avg_rating', 'check_availability','starter')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [CarImagesInline]

class CarBookAdmin(admin.ModelAdmin):
    list_display = ['car', 'in_progress']



admin.site.register(CarBook, CarBookAdmin)
admin.site.register(CarImages)
admin.site.register(CarReview)
admin.site.register(Category)
