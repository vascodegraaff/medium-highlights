from django.shortcuts import render, redirect

import requests
requests.packages.urllib3.disable_warnings()


from datetime import date, timedelta
from bs4 import BeautifulSoup
from .models import Article, Tag
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

#for models to import tags
def index(request):
    allCategories = Tag.objects.all()
    context = {'allCategories':allCategories}
    return render(request, 'index.html', context)


def categories(request):
    allCategories = Tag.objects.all()
    context = {'allCategories':allCategories}
    return render(request, 'category.html', context)

def tagList(request, tag_value):
    category_list = Article.objects.filter(tag=tag_value)
    allCategories = Tag.objects.all()
    context = {'category_list': category_list, 'allCategories': allCategories}
    return render(request, 'tag.html', context)

def topWeekly(request):
    topArticles = Article.objects.order_by('-claps')[:50]
    allCategories = Tag.objects.all()
    context = {'topArticles': topArticles, 'allCategories': allCategories}
    
    return render(request, 'index.html', context)
def scrape(request):
    Article.objects.all().delete()
    dayb4last = date.today()- timedelta(days=2)
    tags = list(Tag.objects.values_list('category',flat=True))
    #tags = ['productivity']
    days = [(dayb4last - timedelta(i)).strftime('%Y/%m/%d') for i in range(7)]
    session = requests.Session()
    session.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
    for tag in tags:
        for day in days:
            archiveUrl = 'https://medium.com/tag/'+ tag + '/archive/' + day
            content =  session.get(archiveUrl, verify=False).content
            soup = BeautifulSoup(content,'html.parser')
            articles = soup.findAll("div", 'postArticle')
            currentDate = day.replace('/','-')
            for article in articles:
                try:
                    authurDetail = article.find('div','postMetaInline-authorLockup')
                    title = article.find('h3','graf').get_text()
                    url = article.find('a','button').get('href')
                    clapStr = article.find('button',{"data-action":"show-recommends"}).get_text()
                    if article.find('a',{"data-action": "show-collection-card"}) != None:
                        publication = article.find('a',{"data-action": "show-collection-card"}).get_text()
                    else:
                        publication = 0
                    authur = authurDetail.find("a",{"data-action": "show-user-card"}).get_text()
                    if 'K' in clapStr:
                        claps = int(float(clapStr.replace('K','')) * 1000)
                    else: 
                        claps = int(clapStr)
                    if claps >= 250:
                        new_article = Article()
                        new_article.title = title
                        new_article.tag = tag
                        new_article.url = url
                        new_article.claps = claps
                        new_article.clapStr = clapStr
                        new_article.authur = authur
                        new_article.publication = publication
                        new_article.date = currentDate
                        new_article.save()
                    
                except AttributeError:
                    pass
    return redirect('/clear')

def clear(request):
    for row in Article.objects.all():
        if Article.objects.filter(title = row.title).count() > 1:
            row.delete()
    return redirect('/')
