from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^500$', views.fivehundred),
    url(r'^500andimeanit$', views.fivehundrederror),
    url(r'^404$', views.fourohfour),
    url(r'^hello$', views.hello),

    url(r'^tasks/create$', views.create_tasks),
    url(r'^tasks$', views.count_tasks)
]
