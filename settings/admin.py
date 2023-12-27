from django.contrib import admin

# Register your models here.
from .models import About, FAQ, Info, NewsLetter
from django_summernote.admin import SummernoteModelAdmin

class AboutAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(About , AboutAdmin)
admin.site.register(Info)
admin.site.register(FAQ)
admin.site.register(NewsLetter)