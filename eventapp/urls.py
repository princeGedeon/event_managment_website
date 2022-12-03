from django.urls import path

from eventapp.views import index,election,EventDetail,paiement

from eventapp.views import EventView

urlpatterns = [

    path('',index,name="home"),
    path('events',EventView.as_view(),name="event"),
    path('events/<str:slug>',EventDetail.as_view(),name="detail_event"),
    path('events/<str:slug>/paiement', paiement, name="pay_event"),
    path('election',election,name="election")

]