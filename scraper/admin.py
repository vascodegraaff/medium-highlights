from django.contrib import admin

# Register your models here.
from .models import Article, Tag

class ArticleAdmin(admin.ModelAdmin):
    list_display=['title','tag','claps','date','publication','url']

admin.site.register(Tag)
admin.site.register(Article,ArticleAdmin)
