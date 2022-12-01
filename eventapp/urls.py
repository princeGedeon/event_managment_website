from django.urls import path

from eventapp.views import index

urlpatterns = [

    path('',index,name="home"),

]