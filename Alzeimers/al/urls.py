from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('index.html', views.index),
    path('index1.html', views.index1),
    path('faq.html',views.faq),
    path('drugs.html',views.drugs),
    path('desc.html',views.desc),
    path('upload.html',views.upload),
    path('Physical test.html',views.test),
    path('doc1.html',views.doc1),
    path('doc2.html',views.doc2),
    path('doc3.html',views.doc3),
    path('call1.html',views.call1),
    path('call2.html',views.call2),
    path('call3.html',views.call3),
    path('loc1.html',views.loc1),
    path('loc2.html',views.loc2),
    path('loc3.html',views.loc3),
    path('signup',views.signup),
    path('signup.html',views.signup),
    path('login.html',views.login),
    path('login',views.login),
]
