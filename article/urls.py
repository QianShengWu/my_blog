from django.conf.urls import url
from article import views
urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^test/$',views.test,name='test'),
]