#maps URL to views functions
from django.urls import path
from . import views

#URL configuration
urlpatterns = [
    path('', views.index),
    path("register/", views.register_request),
    path("account/", views.accType_request),
    path("login/", views.login_request),
    path("logout/", views.logout_request),
    path("promoter/", views.pro_req), #unfinished
    path("venue/", views.venue_req),
    path("venue/concert", views.concert_req),
    path("browse/", views.browse_req),
    path("browse/buy/<int:id_>", views.ticket_req),
    path("mytickets/", views.myTicket_req),
    path("balance/", views.my_balance)
    #path("sell/<int:id_>", views.sell_req)

]
