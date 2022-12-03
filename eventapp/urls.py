from django.urls import path

from eventapp.views import index

from eventapp.views import EventView

urlpatterns = [

    path('',index,name="home"),
    path('events',EventView.as_view(),name="event")

]