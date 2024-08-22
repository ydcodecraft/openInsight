from django.urls import path

from .views.club_views import ClubListView, ClubCreateView
from .views.stadium_views import StadiumListView, StadiumCreateView
from . import views

urlpatterns = [
    path("club/", ClubListView.as_view(), name='list_club'),
    path("club/create", ClubCreateView.as_view()),
    path("stadium/", StadiumListView.as_view(), name='list_stadium'),
    path("stadium/create", StadiumCreateView.as_view()),
]