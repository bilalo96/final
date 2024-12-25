from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from tof.admin import TofAdmin , TranslationTabularInline

# Register your models here.
from .models import Post,Category



class PostAdmin(TofAdmin):  # instead of ModelAdmin
    inlines = (TranslationTabularInline,)

admin.site.register(Post,PostAdmin)
admin.site.register(Category)

