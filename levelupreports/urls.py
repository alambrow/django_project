from levelupreports.views.events.eventsbyuser import userevent_list
from django.urls import path
from .views import usergame_list, userevent_list

urlpatterns = [
    path('reports/usergames', usergame_list),
    path('reports/eventsbyuser', userevent_list)
]
