#!/usr/bin/python
#-*-coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# from firstblog.models import Character
from . import models

# 简单的接口
def index(request):
    articles = models.Articles.objects.all()
    return render(request, 'blog/indexpage.html', { 'articles': articles })

def article_page(request, article_id):
    article = models.Articles.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', { 'article': article })

def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    article = models.Articles.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', { 'article': article })

def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')

    if article_id == '0':
        models.Articles.objects.create(title=title, content=content)
        articles = models.Articles.objects.all()
        return render(request, 'blog/indexpage.html', { 'articles': articles })

    article = models.Articles.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    # return render(request, 'blog/article_page.html', { 'article': article })
    return null

def test(request):
    return HttpResponse('hello world')