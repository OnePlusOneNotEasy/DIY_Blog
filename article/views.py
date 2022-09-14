from django.shortcuts import render
from django.http import HttpResponse
from .models import ArticlePost
import markdown
# Create your views here.
def article_list(request):
    articles = ArticlePost.objects.all()
    context = {'articles': articles}
    return render(request, 'article/list.html', context)

def article_detail(request, id):
    # 取出相应的文章
    article = ArticlePost.objects.get(id=id)

    article.body = markdown.markdown(article.body,
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ]
    )
    # 需要传递给模板的对象
    context = { 'article': article }
    # 载入模板，并返回context对象
    return render(request, 'article/detail.html', context)
