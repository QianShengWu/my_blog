from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from article.models import Article
def home(request):
 	post_list = Article.objects.all()
 	return render(request,'article/home.html',{'post_list':post_list})
def detail(request,article_id):
	article=Article.objects.all()[int(article_id)]
	s="title=%s,category=%s,datatime=%s,content=%s" %(article.title,article.category,article.date_time,article.content)
	return HttpResponse(s)

def test(request):
	return render(request,'article/test.html',{'current_time':datetime.now()})