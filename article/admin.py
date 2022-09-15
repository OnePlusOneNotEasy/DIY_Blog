from django.contrib import admin
from .models import ArticlePost, ArticleColumn
# Register your models here.

admin.site.register(ArticlePost)
# 注册文章栏目
admin.site.register(ArticleColumn)
