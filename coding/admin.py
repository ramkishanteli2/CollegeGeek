from django.contrib import admin
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_id', 'category_name']


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['article_id', 'article_heading',
                    'publish_date', 'category']


admin.site.register(Article, ArticleAdmin)
