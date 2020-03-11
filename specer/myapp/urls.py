from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('detail', views.detail, name='detail'),
    path('club', views.club, name='club'),
    path('contact', views.contact, name='contact'),
    path('main', views.main, name='main'),
    path('result', views.result, name='result'),
    path('schedule', views.schedule, name='schedule'),
]

